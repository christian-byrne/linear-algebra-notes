from chapter01_vector.vector_class import Vector
from chapter01_vector.matrix_class import Matrix
from chapter05_orthogonality.graham_schmidt_orthogonality import GrahamSchmidt

from typing import List


class LeastSquaresSolution:
    def __init__(self, vectors: List[Vector], constant_vector: Vector):
        self.constant_vector = constant_vector
        constant_vector.print("Constant")

        self.vectors = Matrix(vectors)
        self.vectors.print("Dependent")

        self.size = len(vectors)

    def dims(self) -> int:
        return len(self.vectors[0])

    def solve(self):
        # Step 1: Separate the constant vector from the dependent vectors
        # in the set by forming a coefficient matrix.
        # ....... TODO: don't understand this part

        # Step 2: Find an orthogonal basis for the column space.
        gs = GrahamSchmidt(self.vectors)
        orthogonals: List[Vector] = gs.orthogonalize().orthogonal_vectors
        Matrix(orthogonals).print("After Orthogonalizing")

        # Step 3: Project the constant vector onto the column space
        # I.e., apply the projectiong of each vector in the orthogonal set
        # onto the constant vector.
        # NOTE: We are projecting the CONSTANT -> ONTO -> SPACE
        projected_vectors = Matrix(
            [self.constant_vector.project(vec) for vec in orthogonals]
        )
        projected_vectors.print("After Projecting Constant Vector onto Orthogonals")

        # Step 4: Sum the projected vectors to get the projected constant vector.
        projected_constant_vector = projected_vectors.sum()

        # Step 5: Construct the least-squares solution which will consist of the
        # original vectors and the projected constant vector.
        return Matrix(self.vectors + [projected_constant_vector])


def example_from_playposit():
    """This uses the `LeaseSquaresSolution` to solve the example problem presented
    in in the PlayPosit video '2.2.3 Column space & computing centrois'
    """

    # The example vectors given in the video.
    example_vectors = [Vector([1, 1, 0]), Vector([1, 0, 1]), Vector([2, 0, 0])]
    # The [2, 0, 0] vector was called the constant vector.
    constant_vector = example_vectors[2]
    # The other two were used to find the orthogonal basis.
    dependent_vectors = example_vectors[:2]

    LeastSquaresSolution(dependent_vectors, constant_vector).solve().print(
        "Least Squares Solution"
    )
