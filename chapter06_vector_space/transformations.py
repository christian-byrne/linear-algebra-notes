import random
from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix
from typing import Tuple
from rich import console, print


def random_matrix(shape: Tuple[int, ...] = None):
    if not shape:
        rows = random.randint(1, 8)
        cols = random.randint(1, 8)
    else:
        rows, cols = shape

    return Matrix([[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)])


def is_linear_transformation(
    function: callable, test_count: int = 50, print_all_tests: bool = False
) -> Tuple[bool, str]:
    """
    Check if the function is a linear transformation.
    """
    for _ in range(test_count):
        test_target = random_matrix()

        scalar = random.randint(0, 32)
        a = function(test_target) * scalar
        b = function(test_target * scalar)

        if print_all_tests:
            if isinstance(a, (Vector, Matrix)):
                a.print("function(input) * scalar")
            else:
                print(f"function(input) * scalar: {a}")
            if isinstance(b, (Vector, Matrix)):
                b.print("function(input * scalar)")
            else:
                print(f"function(input * scalar): {b}")
            print()

        if a != b:
            print("\n\na != b\n\n")
            return False

        # c = function(test_target) + scalar
        # d = function(test_target + scalar)
        # print(c)
        # print(d)

        # if c != d:
        #     return False

    return True, f"{function.__name__} is a linear transformation!"


def playposit_example_1():
    """Example from video 3.1.1 Linear Transformations

    C: 3-space -> 2-space
    given by the formula [a, b, c] -> [0, 0]
    """

    def C(matrix: Matrix):
        return Matrix([[0, 0]])

    print(is_linear_transformation(C))


def playposit_example_2():
    """Example from video 3.1.1 Linear Transformations

    D: 2-space -> 2-space
    given by the formula [a, b] -> [a + 1, b]
    """

    def D(matrix: Matrix):
        return Matrix([[vec[0] + 1] + vec[1:] for vec in matrix.vectors])

    print(is_linear_transformation(D, print_all_tests=True))
