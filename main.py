import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from chapter01_vector.vector_class import Vector
from chapter01_vector.point_to_line import distance_point_to_line
from chapter03_matrix.matrix_class import Matrix
from chapter05_orthogonality.gram_schmidt_orthogonality import GramSchmidt
from chapter05_orthogonality.least_squares import LeastSquaresSolution, example_from_playposit
from chapter06_vector_space.is_linearly_independent import LinearDependenceTest
from chapter06_vector_space.transformations import *

x = Vector([1, 0, 1])
y = Vector([2, 3, 0])
z = Vector([1, 0, 1])
u = Vector([2**(1/2), 1, -1])
v = Vector([0, 2, -2])

m = Matrix([x, y, z, u, v])


# playposit_example_1()
webassign_problem_4()