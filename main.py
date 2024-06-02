import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from chapter01_vector.vector_class import Vector
from chapter05_orthogonality.graham_schmidt_orthogonality import GrahamSchmidt
from chapter06_vector_space.is_linearly_independent import LinearDependenceTest
from chapter05_orthogonality.least_squares import LeastSquaresSolution, example_from_playposit

x = Vector([1, 0, 1])
y = Vector([2, 3, 0])
z = Vector([1, 0, 1])

example_from_playposit()
