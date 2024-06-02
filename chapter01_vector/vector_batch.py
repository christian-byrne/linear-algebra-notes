from chapter01_vector.vector_class import Vector

from rich.panel import Panel
from rich.table import Table
from rich import print
from typing import List


class VectorBatch:
    """Class for creating and managing a batch of Vector instances"""

    def __init__(self, array_2d: List[List[int]] = []):
        self.vectors = [Vector(array) for array in array_2d]

    def dim(self) -> int:
        return max([vector.size for vector in self.vectors])

    def append(self, new_vector: Vector) -> "VectorBatch":
        """Add a new vector to the batch. If it is an array it will be converted
        to a `Vector` automatically"""
        if not isinstance(new_vector, Vector):
            new_vector = Vector(new_vector)

        self.vectors.append(new_vector)
        return self

    def clear(self) -> "VectorBatch":
        self.vectors = []
        return self

    def sum(self) -> Vector:
        """Sum all the vectors in the batch and return the sum as a `Vector`"""
        result = Vector([0 for _ in range(self.dim())])
        for vec in self.vectors:
            result = result + vec

        return result

    def __add__(self, other) -> "VectorBatch":
        new_vecs = self.vectors + other
        return VectorBatch(new_vecs)

    def __contains__(self, test_vector: Vector) -> bool:
        return any([vec == test_vector for vec in self.vectors])

    def __getitem__(self, index: int) -> Vector:
        return self.vectors[index]

    def __iter__(self):
        return iter(self.vectors)

    def __str__(self):
        return f"{[vec.coordinates for vec in self.vectors]}"
    
    def __repr__(self):
        return f"VectorBatch({[vec.coordinates for vec in self.vectors]})"

    def print(self, title: str = "") -> str:
        if title:
            print(
                Panel(
                    f"[bold]Vector Batch - {title}[/bold]",
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
