from typing import List
from chapter03_matrix.matrix_class import Matrix

def matrix_inverse(matrix: Matrix) -> Matrix:
    if not matrix.is_square():
        raise ValueError("Matrix must be square to have an inverse.")
    if matrix.determinant() == 0:
        raise ValueError("Matrix must have a non-zero determinant to have an inverse.")
    identity = Matrix.identity(matrix.rows)
    augmented = Matrix(matrix.matrix + identity.matrix)
    augmented.gauss_jordan()
    return Matrix([row[matrix.cols:] for row in augmented.matrix])