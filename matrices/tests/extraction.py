

from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix


x = Vector([1, 0, 1])
y = Vector([2, 3, 0])
z = Vector([1, 0, 1])
u = Vector([2 ** (1 / 2), 1, -1])
v = Vector([0, 2, -2])

m = Matrix([x, y, z, u, v])
xm = Matrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
ym = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

rm = Matrix([[2, 3, 4], [1, 2, 3], [2, 2, 2]])

count_sqm = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

zmc = Matrix([[1, 2, 3], [4, 5, 6]])
zmr = Matrix([[1, 2], [3, 4], [5, 6]])


def iterative_cleave_test(cleave_row=0, cleave_col=0):
  """This is a way to isolate partitions by setting every value outside the partition to 0. Using
  the extractor method."""
  count_sqm.print("Original Matrix")

  # Get the inverse extractor for the given row
  eb1 = count_sqm.get_extractor_multiple(cleave_row, 0, inverse=True)
  eb1.print(f"Inverse Extractor for Row #{cleave_row + 1}")

  # Get the inverse extractor for the given column
  eb2 = count_sqm.get_extractor_multiple(cleave_col, 1, inverse=True)
  eb2.print(f"Inverse Extractor for Column #{cleave_col + 1}")

  extractor_product: Matrix = eb1 * eb2
  extractor_product.print("Product of Extractors")

  masked = extractor_product.element_wise_product(count_sqm)
  masked.print("Masked Matrix")


def inverse_extraction_test():
  rm.print("Original Matrix")
  extractor_matrix = rm.get_extractor_multiple(1, 1, inverse=True)
  extractor_matrix.print("Extractor Matrix ofr Inverse Extraction of Col2")
  # rm.extract_row_or_col(1, 1, inverse=True).print("Inverse Extracted Column #2")

def extraction_test():
  zmc.print("Original Matrix")
  zmc.extract_row_or_col(1, 1, inverse=False).print("Extracted Column #2")
  zmc.extract_row_or_col(2, 0, inverse=False).print("Extracted Row #3")
  zmc.extract_row_or_col(0, 0, inverse=False).print("Extracted Row #1")


