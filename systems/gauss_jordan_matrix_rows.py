from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix



def mirror_onto_identity_decorator(func):
    def wrapper(self, *args):
        if self.is_identity():
            return func(self, *args)
        else:
            self.mirror_onto_identity()
            result = func(self, *args)
            self.mirror_onto_original()
            return result
    return wrapper


class MatrixRows(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)

    def row_swap(self, row1, row2):
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]

    def row_multiply(self, row, scalar):
        self.matrix[row] = Vector([scalar * i for i in self.matrix[row]])

    def row_add(self, row1, row2, scalar):
        self.matrix[row1] = [self.matrix[row1][i] + scalar * self.matrix[row2][i] for i in range(len(self.matrix[row1]))]