from chapter01_vector.vector_class import Vector

from rich.panel import Panel
from rich.table import Table
from rich import print
from typing import List, Union, Tuple


def apply_to_identity(method: callable):
    """To create the inverse of a transformation, apply to the identity matrix every operation that
    was applied to the original matrix. Then use the modified identity matrix to revert the
    transformation."""

    def wrapper(self: "Matrix", *args, **kwargs):
        original_result = method(self, *args, **kwargs)

        if not isinstance(original_result, Matrix):
            return original_result

        if self.transformation_invert.shape() != original_result.shape():
            print(
                f"Matrix shape mismatch: {self.transformation_invert.shape()} != {original_result.shape()}"
            )
            return original_result

        identity_result = method(self.transformation_invert, *args, **kwargs)
        self.transformation_invert = identity_result

        return original_result

    return wrapper


class Matrix:
    """Matrix-like collection of Vectors."""

    def __init__(
        self,
        components: List[Union[List[int], List[Vector], int, float, complex]] = None,
        original: bool = True
    ):
        if not components:
            self.vectors = []
        elif isinstance(components[0], Vector):
            self.vectors = components
        elif isinstance(components[0], list):
            self.vectors = [Vector(array) for array in components]
        elif isinstance(components, self.__class__):
            self.vectors = components.vectors
        elif isinstance(components, (int, float, complex)):
            self.vectors = [Vector([components])]
        else:
            raise TypeError("Invalid type for Matrix initialization")

        self.original = original
        if self.original:
            self.transformation_invert = Matrix(
                [[1 if i == j else 0 for j in range(self.shape()[1])] for i in range(self.shape()[0])],
                original=False
            )

    def extract_row_or_col(
        self, index: int, axis: int, inverse: bool = False
    ) -> "Matrix":
        """
        Multiplication of a matrix by a standard unit vector can "pick out" or "reproduce"
        a column or row of the matrix.

        If `inverse`, extract all other rows or columns except the one at `index`.

        Theorem:
            Let A be an m x n matrix, e_i a standard 1 x m unit vector, and
            e_j a standard 1 x n unit vector.
            > e_i * A is the ith row of A
            > A * e_j is the jth column of A.

        [see example](./column_extraction_examples.py)

        """
        extractor: self.__class__ = self.get_extractor_multiple(index, axis, inverse)
        # extractor.print(f"Extractor for {index} on axis {axis}")
        if axis == 0:
            return self * extractor
        elif axis == 1:
            return extractor * self

    def get_extractor_multiple(
        self, index: int, axis: int, inverse: bool = False
    ) -> "Matrix":
        on_val = 1 if not inverse else 0
        off_val = 0 if not inverse else 1

        if axis == 0:
            extractor_matrix = Matrix(
                [
                    Vector([on_val if i == index else off_val])
                    for i in range(self.shape()[1])
                ]
            )
        elif axis == 1:
            extractor_matrix = Matrix(
                [
                    Vector(
                        [
                            on_val if i == index else off_val
                            for i in range(self.shape()[0])
                        ]
                    )
                ]
            )

        return extractor_matrix

    def is_generalized_inverse_relative_to(self, other: "Matrix") -> bool:
        original = Matrix(self.vectors[:])

        return original * other * original == original

    def is_psuedo_inverse(self) -> bool:
        pass

    def is_commutative_with(self, other: "Matrix") -> bool:
        """Check if the matrix is commutative with another matrix."""
        original = Matrix(self.vectors[:])

        product_lr = original * other
        product_rl = other * original

        return product_lr == product_rl

    def is_identity(self) -> bool:
        """Check if the matrix is an identity matrix."""
        if len(self.vectors) != len(self.vectors[0]):
            return False
        for i, vec in enumerate(self.vectors):
            if vec[i] != 1:
                return False
            if any([vec[j] != 0 for j in range(len(vec)) if j != i]):
                return False
        return True

    def compute_shape(self, vectors: Union[List, Tuple]) -> Tuple[int, ...]:
        vectors = vectors[:]
        shape = []
        while isinstance(vectors, (list, Vector, self.__class__)):
            if isinstance(vectors, Vector):
                shape.append(vectors.size)
                break
            elif isinstance(vectors, self.__class__):
                shape.append(len(vectors))
                vectors = vectors.vectors
            elif isinstance(vectors, list):
                shape.append(len(vectors))
                if isinstance(vectors[0], (int, float, complex)):
                    shape.append(len(vectors[0]))
                    break
                vectors = vectors[0] if len(vectors) > 0 else []
            else:
                shape.append(1)
                break
        return tuple(shape)

    def dims(self) -> Tuple[int, ...]:
        return self.compute_shape(self.vectors)[0]

    def shape(self) -> Tuple[int, ...]:
        return self.compute_shape(self.vectors)

    def size(self, index: int) -> int:
        if isinstance(self.vectors, list):
            return len(self.vectors[index])
        else:
            raise TypeError("Scalar has no size property")

    def append(self, new_vector: Vector) -> "Matrix":
        """Add a new vector to the matrix. If it is an array it will be converted
        to a `Vector` automatically"""
        if not isinstance(new_vector, Vector):
            new_vector = Vector(new_vector)

        self.vectors.append(new_vector)
        return self

    def clear(self) -> "Matrix":
        self.vectors = []
        return self

    def transpose(self) -> "Matrix":
        return Matrix(
            [self.vectors[j][m] for j in range(len(self.vectors))]
            for m in range(len(self.vectors[0]))
        )

    @apply_to_identity
    def __mul__(
        self, other: Union[List[Vector], List[List[int]], int, float]
    ) -> "Matrix":
        # Scalar multiplication.
        if isinstance(other, (int, float, complex)):
            return Matrix(
                [[component * other for component in vec] for vec in self.vectors]
            )
        # Matrix multiplication (dot product).
        if isinstance(other, self.__class__):
            return Matrix(
                [
                    [
                        sum(
                            [
                                self.vectors[i][k] * other.vectors[k][j]
                                for k in range(len(self.vectors[0]))
                            ]
                        )
                        for j in range(len(other.vectors[0]))
                    ]
                    for i in range(len(self.vectors))
                ]
            )

    def __add__(self, other: Union[List[Vector], "Matrix", Vector]) -> "Matrix":
        if isinstance(other, list):
            return Matrix(self.vectors + other)
        elif isinstance(other, Vector):
            return Matrix(self.vectors).append(other)
        elif isinstance(other, self.__class__):
            return Matrix(self.vectors + other.vectors)
        elif isinstance(other, (float, int, complex)):
            # Element-wise addition
            return Matrix([self_vec + other for self_vec in self.vectors])

    def __sub__(self, other: Union[List[Vector], "Matrix", Vector]) -> "Matrix":
        if isinstance(other, list):
            difference = [
                vec
                for vec in self.vectors
                if not any([vec == other_vec for other_vec in other])
            ]
            return Matrix(difference[:])
        elif isinstance(other, Vector):
            difference = [vec for vec in self.vectors if vec != other]
            return Matrix(difference[:])
        elif isinstance(other, self.__class__):
            return Matrix(
                [
                    self_vec - other_vec
                    for self_vec, other_vec in zip(self.vectors, other.vectors)
                ]
            )
        elif isinstance(other, (float, int, complex)):
            # Element-wise subtraction
            return Matrix([self_vec - other for self_vec in self.vectors])

    def sum(self) -> Vector:
        """Sum all the vectors in the matrix and return the sum as a `Vector`"""
        result = Vector([0 for _ in range(self.shape()[1])])
        for vec in self.vectors:
            result = result + vec

        return result

    def element_wise_product(self, other: "Matrix") -> "Matrix":
        if self.shape() != other.shape():
            raise ValueError(
                "Matrices must have the same shape for element-wise product"
            )

        return Matrix(
            [
                [
                    self_compnent * other_compnent
                    for self_compnent, other_compnent in zip(self_vecc, other_vec)
                ]
                for self_vecc, other_vec in zip(self.vectors, other.vectors)
            ]
        )

    def __eq__(self, other: "Matrix"):
        for self_vec, other_vec in zip(self.vectors, other.vectors):
            if self_vec != other_vec:
                return False
        return True

    def __len__(self) -> int:
        return len(self.vectors)

    def __contains__(self, test_vector: Vector) -> bool:
        return any([vec == test_vector for vec in self.vectors])

    def __getitem__(self, index: int) -> Vector:
        return self.vectors[index]

    def __iter__(self):
        return iter(self.vectors)

    def __str__(self):
        return f"{[vec.coordinates for vec in self.vectors]}"

    def __repr__(self):
        return f"Matrix({[vec.coordinates for vec in self.vectors]})"

    def print(self, title: str = "") -> str:
        if title:
            print(
                Panel(
                    f"[bold]Matrix - {title}[/bold]".replace("->", "→"),
                    style="green",
                    expand=False,
                    border_style="dim white",
                )
            )
        tb = Table(style="dim cyan", show_header=False)
        rows = self.shape()[0]
        cols = self.shape()[1]

        for i in range(rows):
            tb.add_column()

        for i in range(cols):
            tb.add_row(*[f"{self.vectors[v].coordinates[i]:.2f}" for v in range(rows)])

        print(tb)
        return self
