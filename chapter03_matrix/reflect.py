import numpy as np

# Sample matrix
matrix = np.array([[0, 1, 1, 1, 0],
                   [0, 0, 0, 0 , 0],
                   [1, 0, 0, 0 , 0],
                   [1, 0, 0, 0 , 0],
                   [0, 0, 0, 0 , 0],
                   [0, 0, 0, 0 , 0]])

# Transpose the matrix
transposed_matrix = np.transpose(matrix)

# Transpose across the other diagonal
transposed_matrix_2 = np.fliplr(matrix)

print("Original Matrix:")
print(matrix)
# print("\nTransposed Matrix:")
# print(transposed_matrix)
# print("\nTransposed Matrix 2:")
# print(transposed_matrix_2)

print(np.flipud(np.fliplr(matrix)))

# print(np.transpose(transposed_matrix_2))
# print(np.logical_and(matrix, matrix))
# print(np.logical_or(matrix, matrix))

# # convert to boolean
# bool_matrix = matrix.astype(bool)
# print(np.dot(bool_matrix, bool_matrix))