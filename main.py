import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from chapter01_vector.vector_class import Vector
from chapter05_orthogonality.graham_schmidt_orthogonality import GrahamSchmidt
from chapter06_vector_space.is_linearly_independent import LinearDependenceTest
from chapter05_orthogonality.least_squares import LeastSquaresSolution, example_from_playposit
from chapter01_vector.point_to_line import distance_point_to_line

x = Vector([1, 0, 1])
y = Vector([2, 3, 0])
z = Vector([1, 0, 1])

u = Vector([2**(1/2), 1, -1])
v = Vector([0, 2, -2])

correct = distance_point_to_line(
  (3, 1, 1),
  (1, 0, 2),
  Vector([-1, 1, 0])
)

xy = Vector([-1, 1, 0])
a = xy.distance_to_point((1, 0, 2))

xy = Vector([-1, 1, 0])
b = xy.distance_to_point((2, 1, 1))

xy = Vector([3, 1, 1])
c = xy.distance_to_point((1, 0, 2))

print(f"correct: {correct}\na: {a}\nb: {b}\nc: {c}")

