import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from chapter01_vector.vector_class import Vector
from chapter01_vector.point_to_line import distance_point_to_line

from chapter03_matrix.matrix_class import Matrix
from chapter03_matrix.mask import mask_minors, create_mask, mask_by_indices
from chapter03_matrix.column_extraction_examples import example_from_textbook_matrices_1
from chapter03_matrix.tests.extraction import (
    extraction_test,
    inverse_extraction_test,
    iterative_cleave_test,
)

from chapter05_orthogonality.gram_schmidt_orthogonality import GramSchmidt
from chapter05_orthogonality.least_squares import (
    LeastSquaresSolution,
    example_from_playposit,
)

from chapter06_vector_space.is_linearly_independent import LinearDependenceTest
from chapter06_vector_space.transformations import (
    playposit_example_1,
    playposit_example_2,
    webassign_problem_4,
)


os.system("clear")

x = Vector([1, 0, 1])
y = Vector([2, 3, 0])
z = Vector([1, 0, 1])
u = Vector([2 ** (1 / 2), 1, -1])
v = Vector([0, 2, -2])

m = Matrix([x, y, z, u, v])
xm = Matrix([[1, 2, 1], [0, 1, 0], [0, 0, 1]])
ym = Matrix([[1, 2, 3], [0, 1, 0], [0, 0, 1]])
zmc = Matrix([[1, 2, 3], [4, 5, 6]])
zmr = Matrix([[1, 2], [3, 4], [5, 6]])

rm = Matrix([[2, 3, 4], [1, 2, 3], [2, 2, 2]])

count_sqm = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



rm.print("Original Matrix")

y = rm * ym

y.print("Result of Multiplication")

r = rm.transformation_invert * y

r.print("Result of Multiplication")
