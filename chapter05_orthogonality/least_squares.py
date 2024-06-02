from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix
from chapter05_orthogonality.gram_schmidt_orthogonality import GramSchmidt

from typing import List, Union


class LeastSquaresSolution:
    def __init__(
        self,
        matrix: Union[Matrix, List[Vector]],
    ):
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

    def solve(self) -> Matrix:
        """Solve the least squares solution for the given matrix."""
        solutions = {}
        for i in range(self.matrix.shape()[0]):
            independent_vectors = (
                self.matrix.vectors[:][:i] + self.matrix.vectors[:][i + 1 :]
            )
            dependent_vector = self.matrix.vectors[:][i]
            ls = LeastSquaresPermutation(independent_vectors, dependent_vector)
            solutions[ls.analyze_fit()] = ls.solve()
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

    def analyze_fit(self):
        """RSS: Residual Sum of Squares. To analyze the fit of the least squares solution.
        The sum of the squared distance between the observed value and the predicted value.
        """
        solution = self.solve()
        total_distance = 0
        for j in range(len(solution.vectors) - 1):
            for i, component in enumerate(solution.vectors[j].coordinates):
                total_distance += (component - solution.vectors[-1].coordinates[i]) ** 2
        return total_distance


def example_from_playposit():
    """This uses the `LeaseSquaresSolution` to solve the example problem presented
    in in the PlayPosit video '2.2.3 Column space & computing centroids'

    """
    # The example vectors given in the video.
    example_vectors = Matrix([Vector([1, 1, 0]), Vector([1, 0, 1]), Vector([2, 0, 0])])

    # The expected answer from the video.
    expected_answer = Matrix([[1, 1, 0], [1, 0, 1], [4 / 3, 2 / 3, 2 / 3]])

    expected_answer.print("Last Squares - Expected Solution")
    LeastSquaresSolution(example_vectors).solve().print(
        "Least Squares - Computed Solution"
    )
