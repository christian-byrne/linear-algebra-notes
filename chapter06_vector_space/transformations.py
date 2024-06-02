import random
from chapter01_vector.vector_class import Vector
from chapter03_matrix.matrix_class import Matrix
from typing import Tuple, Union, List, Any
from rich import console, print


def random_matrix(shape: Tuple[int, ...] = None):
    if not shape:
        rows = random.randint(1, 8)
        cols = random.randint(1, 8)
    else:
        rows, cols = shape

    return Matrix([[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)])


def is_onto():
    return True


def is_one_to_one():
    return True


def is_invertible():
    return is_onto() and is_one_to_one()


def is_homogenous_transformation(
    relation: callable,
    scalar: Union[float, int, complex],
    target: Union[Matrix, Vector],
    verbose: bool,
):
    a: Union[Vector, Matrix, Any] = relation(target) * scalar
    b: Union[Vector, Matrix, Any] = relation(target * scalar)

    if verbose:
        if isinstance(a, (Vector, Matrix)):
            a.print(f"{relation.__name__}(input) * scalar")
        else:
            print(f"{relation.__name__}(input) * scalar: {a}")
        if isinstance(b, (Vector, Matrix)):
            b.print(f"{relation.__name__}(input * scalar)")
        else:
            print(f"{relation.__name__}(input * scalar): {b}")
        print()

    if a != b:
        return False
    return True


def is_additive_transformation(
    relation: callable,
    target: Union[Matrix, Vector],
    verbose: bool,
):
    a: Union[Vector, Matrix, Any] = relation(target) + relation(target)
    b: Union[Vector, Matrix, Any] = relation(target + target)

    if verbose:
        if isinstance(a, (Vector, Matrix)):
            a.print(f"{relation.__name__}(input) + {relation.__name__}(input)")
        else:
            print(f"{relation.__name__}(input) + {relation.__name__}(input): {a}")
        if isinstance(b, (Vector, Matrix)):
            b.print(f"{relation.__name__}(input + input)")
        else:
            print(f"{relation.__name__}(input + input): {b}")
        print()

    if a != b:
        return False
    return True


def is_linear_transformation(
    function: callable, test_count: int = 50, print_all_tests: bool = False
) -> Tuple[bool, str]:
    """
    Check if the relation is a linear transformation by brute force.

    """
    success_msg = True, f"{function.__name__} is a linear transformation!"
    failure_msg = False, f"{function.__name__} is not linear transformation."
    for i in range(test_count):
        test_target = random_matrix()

        # Step 1: Test homoegeneity.
        scalar = random.randint(0, 32)
        if not is_homogenous_transformation(function, scalar, test_target, print_all_tests):
            print(f"Failed on homogeneity test # {i}\nwhile comparing {a} with {b}\n")
            return failure_msg

        # Step 2: Test additivity.
        if not is_additive_transformation(function, test_target, print_all_tests):
            print(f"Failed on additivity test # {i}\nwith {test_target}\n")
            return failure_msg
    
    return success_msg


def webassign_problem_4():
    # T: R^2 -> R^2
    # maps [[4, 3], [1, -1]] to [[0, -1], [0, 3]]
    # {[4, 3], [0, -1]} form a basis for R^2
    #
    # Find T([1, 0])
    #
    # Write [1, 0] as a linear combination of the basis elements.
    # 4a = 1 -> a = 1/4
    # 3a - b = 0 -> b = 3/4
    # [1, 0] ~ [1/4 [4, 3], 3/4 [0, -1]]
    #
    # Since T is a linear transformation, property:
    # T(1/4 [4, 3] + 3/4 [1, -1]) = T(1/4 [4, 3]) + T(4/3 [1, -1])
    #
    # T([4, 3]) = [1, -1] -> T(1/4 [4, 3]) = 1/4 T([4, 3]) = 1/4 [1, -1] = [1/4, -1/4]
    # T([0, -1]) = [0, 3] -> T(3/4 [0, -1]) = 3/4 T([0, -1]) = 3/4 [0, 3] = [0, 9/4]
    #
    #
    pass


def playposit_example_1():
    """Example from video 3.1.1 Linear Transformations

    C: 3-space -> 2-space
    given by the formula [a, b, c] -> [0, 0]
    """

    def C(matrix: Matrix):
        return Matrix([[0, 0]])

    print(is_linear_transformation(C, print_all_tests=False))


def playposit_example_2():
    """Example from video 3.1.1 Linear Transformations

    D: 2-space -> 2-space
    given by the formula [a, b] -> [a + 1, b]
    """

    def D(matrix: Matrix):
        return Matrix([[vec[0] + 1] + vec[1:] for vec in matrix.vectors])

    print(is_linear_transformation(D, print_all_tests=True))
