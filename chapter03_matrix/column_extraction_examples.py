from chapter03_matrix.matrix_class import Matrix


def example_from_textbook_matrices_1():
    """From the section on matrix multiplication in the textbook, concerning "extracting" or "picking out" columns/rows from a matrix."""
    # First example matrix from textbook.
    zm = Matrix(
        [
            [4, 2, 1],
            [0, 5, -1],
        ]
    )

    expected_extractor = Matrix([[0], [0], [1]])
    expected_extractor.print("Expected Extractor from Textbook")

    generated_extractor = zm.get_extractor_multiple(2, 1)
    generated_extractor.print("Computed Extractor")

    expected_result = Matrix([[1], [-1]])
    expected_result.print("(Expected) Extracted Column")

    calculated_result = zm * generated_extractor
    calculated_result.print("(Computed) Extracted Column")

    # Second example matrix from textbook.
    expected_extractor = Matrix(
        [
            [0, 1],
        ]
    )
    expected_extractor.print("Expected Extractor from Textbook")

    generated_extractor = zm.get_extractor_multiple(1, 0)
    generated_extractor.print("Computed Extractor")

    expected_result = Matrix(
        [
            [0, 5, -1],
        ]
    )
    expected_result.print("(Expected) Extracted Column")

    calculated_result = generated_extractor * zm
    calculated_result.print("(Computed) Extracted Column")
