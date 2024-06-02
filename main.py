import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from chapter01_vector.vector_class import Vector
from chapter01_vector.point_to_line import distance_point_to_line
from chapter03_matrix.matrix_class import Matrix
from chapter05_orthogonality.graham_schmidt_orthogonality import GrahamSchmidt
from chapter06_vector_space.is_linearly_independent import LinearDependenceTest
from chapter05_orthogonality.least_squares import LeastSquaresSolution, example_from_playposit

x = Vector([1, 0, 1])
y = Vector([2, 3, 0])
z = Vector([1, 0, 1])
u = Vector([2**(1/2), 1, -1])
v = Vector([0, 2, -2])

mx = Matrix([
  [1, 2, 3],
  [1, 0, 2],
  [4, 3, 7]
])

mx.print("Original Matrix")

res = mx.transpose()
res.print("Transposed")