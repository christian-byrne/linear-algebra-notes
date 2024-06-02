from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix
from chapter05_orthogonality.gram_schmidt_orthogonality import GramSchmidt

from rich.panel import Panel
from rich.console import Group
from rich import print
from typing import List, Union
import numpy as np


class LeastSquaresSolution:
    def __init__(
        self,
        matrix: Union[Matrix, List[Vector]],
        verbose: bool = False,
    ):
        self.verbose = verbose
        if isinstance(matrix, Matrix):
            self.matrix = matrix
        elif isinstance(matrix, list) and isinstance(matrix[0], Vector):
            self.matrix = Matrix(matrix)
        elif isinstance(matrix, list) and isinstance(matrix[0], list):
            self.matrix = Matrix([Vector(vec) for vec in matrix])
        elif matrix == 0:
            self.matrix = Matrix()
        else:
            raise TypeError("Invalid type for matrix")

    def solve(self, print_all: bool = False) -> Matrix:
        """
        Solve the least squares solution for the given matrix.

        Find the LS solution for each permutation of the matrix columns.

        Analyze the solution for each permutation by finding the solution to the system
        of equations described by each describe least squares matrix solution then find
        the sum of the squared distances from that point to each of the original vectors.

        Return the solution with the smallest sum of squared distances.
        """
        solutions = {}
        for i in range(self.matrix.shape()[0]):
            independent_vectors = (
                self.matrix.vectors[:][:i] + self.matrix.vectors[:][i + 1 :]
            )
            dependent_vector = self.matrix.vectors[:][i]
            ls = LeastSquaresPermutation(independent_vectors, dependent_vector)
            res_matrix = ls.solve()

            # Re-arrange the solution to match the original matrix
            new_constant = res_matrix.vectors[-1]
            re_arranged_vectors = res_matrix.vectors[:][:-1]
            re_arranged_vectors.insert(i, new_constant)
            res_matrix.vectors = re_arranged_vectors

            constants = np.array(res_matrix.vectors[-1].coordinates)
            np_columns = [np.array(vec.coordinates) for vec in res_matrix.vectors[:-1]]
            coefficients = np.column_stack(np_columns)

            if self.verbose:
                messages = [f"Coefficients: {coefficients}\nConstants: {constants}"]

            try:
                solution_, residuals, rank, s = np.linalg.lstsq(
                    coefficients, constants, rcond=None
                )
                if self.verbose:
                    messages.append(
                        f"Rank: {rank}\nSingular Values: {s}\nResiduals: {residuals}\nSolution: {solution_}"
                    )

                permutation_fit_score = 0
                for vec in self.matrix.vectors:
                    # Scale the coefficients by the solution
                    coefficient_sum = 0
                    for i in range(len(solution_)):
                        coefficient_sum += vec.coordinates[i] * solution_[i]

                    # Subtract the constant term
                    coefficient_sum -= vec.coordinates[-1]

                    # Find the distance from the point to the plane
                    distance = abs(coefficient_sum) / vec.norm()

                    # Add the squared distance to the total distance
                    permutation_fit_score += distance**2

            except np.linalg.LinAlgError:
                # No solution found
                permutation_fit_score = np.inf

            solutions[permutation_fit_score] = res_matrix
            if self.verbose:
                print(Panel(Group(*messages), title="LeastSquares Details"))

            if print_all:
                res_matrix.print(
                    f"Least Squares Solution when column #{i} {dependent_vector.coordinates} is constant\nRSS Score: {permutation_fit_score}"
                )

        return solutions[min(solutions.keys())]


class LeastSquaresPermutation:
    def __init__(
        self,
        matrix: Union[Matrix, List[Vector]],
        constant_vector: Union[Vector, list[Union[int, float, complex]]],
        verbose: bool = False,
    ):
        self.verbose = verbose
        if isinstance(matrix, Matrix):
            self.matrix = matrix
        elif isinstance(matrix, list) and isinstance(matrix[0], Vector):
            self.matrix = Matrix(matrix)
        elif isinstance(matrix, list) and isinstance(matrix[0], list):
            self.matrix = Matrix([Vector(vec) for vec in matrix])
        elif matrix == 0:
            self.matrix = Matrix()
        else:
            raise TypeError("Invalid type for matrix")
        if self.verbose:
            self.matrix.print("Dependent Vectors")

        if isinstance(constant_vector, Vector):
            self.constant_vector = constant_vector
        elif isinstance(constant_vector, list):
            self.constant_vector = Vector(constant_vector)
        elif isinstance(constant_vector, (int, float, complex)):
            self.constant_vector = Vector(
                [constant_vector for _ in range(self.matrix.dims()[1])]
            )
        if self.verbose:
            self.constant_vector.print("Constant Vector")

        self.originals = Matrix(self.matrix.vectors[:] + [self.constant_vector])

    def solve(self):
        # Step 1: Separate the constant vector from the dependent vectors
        # in the set by forming a coefficient matrix.
        # ....... TODO: don't understand this part

        # Step 2: Find an orthogonal basis for the column space.
        gs = GramSchmidt(self.matrix)
        orthogonals: List[Vector] = gs.orthogonalize().orthogonal_vectors
        if self.verbose:
            Matrix(orthogonals).print("After Orthogonalizing")

        # Step 3: Project the constant vector onto the column space
        # I.e., apply the projectiong of each vector in the orthogonal set
        # onto the constant vector.
        # NOTE: We are projecting the CONSTANT -> ONTO -> SPACE
        projected_vectors = Matrix(
            [self.constant_vector.project(vec) for vec in orthogonals]
        )
        if self.verbose:
            projected_vectors.print("After Projecting Constant Vector onto Orthogonals")

        # Step 4: Sum the projected vectors to get the projected constant vector.
        projected_constant_vector = projected_vectors.sum()

        # Step 5: Construct the least-squares solution which will consist of the
        # original vectors and the projected constant vector.
        return Matrix(self.matrix.vectors + [projected_constant_vector])


def example_from_playposit():
    """This uses the `LeaseSquaresSolution` to solve the example problems presented
    in the PlayPosit videos '2.2.3 Column space & computing centroids' and
    '2.2.3 Supplemented...'.

    """
    print("\nExample from Video 2.2.3 Column space & computing centroids")
    # The example vectors given in first the video.
    example_vectors = Matrix([[1, 1, 0], [1, 0, 1], [2, 0, 0]])
    example_vectors.print("Original Vectors")

    # The expected answer from the first video.
    expected_answer = Matrix([[1, 1, 0], [1, 0, 1], [4 / 3, 2 / 3, 2 / 3]])
    expected_answer.print("Last Squares - Expected Solution")

    LeastSquaresSolution(example_vectors).solve().print(
        "Least Squares - Computed Solution"
    )

    print(
        "\nExample from Video 2.2.3 Supplemental Discussion about Least Squares Solutions"
    )
    # The example vectors given in the second video.
    example_vectors = Matrix(
        [
            [1 / 2, 1, 2],
            [1, 1, 1],
            [1, 2, 2],
        ]
    )
    example_vectors.print("Original Vectors")

    # The expected answer from the second video.
    expected_answer = Matrix(
        [
            [1 / 2, 1, 2],
            [1, 1, 1],
            [9 / 7, 11 / 7, 15 / 7],
        ]
    )
    expected_answer.print("Last Squares - Expected Solution")

    LeastSquaresSolution(example_vectors, verbose=True).solve(print_all=True).print(
        "Least Squares - Computed Solution"
    )
