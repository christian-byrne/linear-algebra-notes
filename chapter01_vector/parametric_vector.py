from chapter01_vector.vector_class import Vector

from typing import Union, List, Tuple, Any


class ParametricVector(Vector):
    """Subclass of Vector that represents a vector scaled by a scalar.
    This way, operations can be done before or after the scaling. Or, the
    scalar can be a stateful or dependent variable.

    """

    def __init__(self, vector: Vector, scalar: Union[float, int, complex] = 1):
        """Default scalar can be 1 due to the axiom of vector spaces which states
        that a vector multiplied by 1 is the vector itself. This is the identity
        element for scalar multiplication.

        """
        self.scalar = scalar
        super().__init__(vector)

    def __call__(self) -> Vector:
        """Return the vector scaled by the scalar/coefficient."""
        return self.__mul__(self.scalar)

    def set_scalar(self, scalar: Union[float, int, complex]):
        self.scalar = scalar

    def get_scalar(self):
        return self.scalar

    def get_vector(self):
        return self.coordinates
