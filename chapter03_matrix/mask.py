from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix

from typing import List


def mask_by_indices(matrix: Matrix, mask_rows: List[int], mask_cols: List[int]):
    """This function creates a mask by setting all values outside the given rows and columns to 0."""
    mask = create_mask(matrix, mask_rows, mask_cols)
    result = matrix.element_wise_product(mask)
    result.print(f"Masked Rows {mask_rows} and Columns {mask_cols}")

    return result


def create_mask(
    matrix: Matrix, mask_rows: List[int], mask_cols: List[int], cur_mask=None
):
    if not mask_rows and not mask_cols:
        return matrix

    if len(mask_rows) == 0:
        target_row_index = 999
    else:
        target_row_index = mask_rows[0]

    if len(mask_cols) == 0:
        target_col_index = 999
    else:
        target_col_index = mask_cols[0]

    row_extractor = matrix.get_extractor_multiple(target_row_index, 0, inverse=True)
    col_extractor = matrix.get_extractor_multiple(target_col_index, 1, inverse=True)

    mask: Matrix = row_extractor * col_extractor
    if cur_mask is not None:
        cur_mask.print("Current Mask")
        mask = mask.element_wise_product(cur_mask)

    return create_mask(mask, mask_rows[1:], mask_cols[1:], mask)


def mask_minors(matrix: Matrix, cleave_row=0, cleave_col=0):
    """This is a way to isolate partitions via masking by setting every value outside
    the partition to 0. Using the extractor method."""
    matrix.print("Original Matrix")

    # Get the inverse extractor for the given row
    eb1 = matrix.get_extractor_multiple(cleave_row, 0, inverse=True)
    eb1.print(f"Inverse Extractor for Row #{cleave_row + 1}")

    # Get the inverse extractor for the given column
    eb2 = matrix.get_extractor_multiple(cleave_col, 1, inverse=True)
    eb2.print(f"Inverse Extractor for Column #{cleave_col + 1}")

    extractor_product: Matrix = eb1 * eb2
    extractor_product.print("Product of Extractors")

    masked = extractor_product.element_wise_product(matrix)
    masked.print("Masked Matrix")
