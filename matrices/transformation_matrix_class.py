from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix

from typing import Tuple, Union, List, Any


class TransformationMatrix(Matrix):
    def __init__(self, vectors: List[Union[List, Tuple, Matrix, Vector]]):
        super().__init__(vectors)

    def determinant(self) -> Any:
        """
        The determinant of a transformation matrix is the volume scaling factor of the transformation.
        """
        if self.shape()[0] == 2 and self.shape()[1] == 2:
            return (
                self.vectors[0][0] * self.vectors[1][1]
                - self.vectors[0][1] * self.vectors[1][0]
            )

        if self.shape()[0] == 3 and self.shape()[1] == 3:
            return (
                self.vectors[0][0] * self.vectors[1][1] * self.vectors[2][2]
                + self.vectors[0][1] * self.vectors[1][2] * self.vectors[2][0]
                + self.vectors[0][2] * self.vectors[1][0] * self.vectors[2][1]
                - self.vectors[0][2] * self.vectors[1][1] * self.vectors[2][0]
                - self.vectors[0][1] * self.vectors[1][0] * self.vectors[2][2]
                - self.vectors[0][0] * self.vectors[1][2] * self.vectors[2][1]
            )
