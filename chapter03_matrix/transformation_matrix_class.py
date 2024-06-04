from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix


from typing import Tuple, Union, List, Any

from rich import console, print

class TransformationMatrix(Matrix):
    def __init__(self, vectors: List[Union[List, Tuple, Matrix, Vector]]):
        super().__init__(vectors)

    def determinant(self) -> Any:
        """
        The determinant of a transformation matrix is the volume scaling factor of the transformation.
        """
        return self.determinant()
