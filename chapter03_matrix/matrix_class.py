from chapter01_vector.vector_class import Vector

from rich.panel import Panel
from rich.table import Table
from rich import print
from typing import List, Union, Tuple


class Matrix:
    """Matrix-like collection of Vectors."""

    def __init__(
        self,
        components: List[Union[List[int], List[Vector], int, float, complex]] = None,
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

        self.shape = self.compute_shape(self.vectors)

    def compute_shape(self, vectors: Union[List, Tuple]) -> Tuple[int, ...]:
        shape = []
        while isinstance(vectors, list):
            shape.append(len(vectors))
            vectors = vectors[0] if len(vectors) > 0 else []
        return tuple(shape)

    def dims(self) -> Tuple[int, ...]:
        return self.shape

    def size(self, index: int) -> int:
        if isinstance(self.vectors, list):
            return len(self.vectors[index])
        else:
            raise TypeError("Scalar has no size property")

    def shape(self) -> Tuple[int, ...]:
        return self.dims()

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

    def __add__(self, other: Union[List[Vector], "Matrix", Vector]) -> "Matrix":
        if isinstance(other, list):
            return Matrix(self.vectors + other)
        elif isinstance(other, Vector):
            return Matrix(self.vectors).append(other)
        elif isinstance(other, self.__class__):
            return Matrix(self.vectors + other.vectors)
        elif isinstance(other, (float, int, complex)):
            # Element-wise addition
            return Matrix(
                [
                    self_vec + other_vec
                    for self_vec, other_vec in zip(self.vectors, other.vectors)
                ]
            )

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
            for i in range(len(self.vectors)):
                self.vectors[i] = self.vectors[i] + other

    def sum(self) -> Vector:
        """Sum all the vectors in the matrix and return the sum as a `Vector`"""
        result = Vector([0 for _ in range(self.dims())])
        for vec in self.vectors:
            result = result + vec

        return result

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
                    f"[bold]Vector Batch - {title}[/bold]".replace("->", "→"),
                    style="green",
                    expand=False,
                    border_style="dim white",
                )
            )
        tb = Table(style="dim cyan", show_header=False)

        rows = self.vectors[0].size

        for i in range(len(self.vectors)):
            tb.add_column()

        for i in range(rows):
            tb.add_row(*[f"{v.coordinates[i]:.2f}" for v in self.vectors])

        print(tb)
        return self
