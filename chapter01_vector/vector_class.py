from typing import List, Union
from rich.table import Table
from rich import print
from rich.panel import Panel


class Vector:
    def __init__(self, coordinates: List[int]):
        self.coordinates = coordinates
        self.size = len(coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def distance_from(self, other: "Vector") -> Union[float, int, complex]:
        """
        The distance between vectors is a direct analogue to the distance 
        between points in space.
        
        Given two vectors $u$ and $v$, the length of the vector that connects the two vectors, $u - v$.
        """

    def is_zero_vector(self) -> bool:
        return all([coord == 0 for coord in self.coordinates])

    def norm(self) -> float:
        return sum([coord**2 for coord in self.coordinates]) ** (1 / 2)

    def project(self, onto: "Vector") -> "Vector":
        coefficient = (self * onto) / (onto * onto)
        return onto.scale(coefficient)

    def orthogonalize(self, onto: "Vector") -> "Vector":
        projection = self.project(onto)
        return self - projection

    def is_orthogonal(self, with_: "Vector") -> bool:
        return self * with_ == 0

    def __eq__(self, other: "Vector") -> bool:
        if isinstance(other, list):
            other_coords = other
        else:
            other_coords = other.coordinates
        return self.coordinates == other_coords

    def __len__(self):
        return self.size

    # ------------- Addition/Subtraction ---------------

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            [
                coord1 - coord2
                for coord1, coord2 in zip(self.coordinates, other.coordinates)
            ]
        )

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            [
                coord1 + coord2
                for coord1, coord2 in zip(self.coordinates, other.coordinates)
            ]
        )

    # -------------- Multiplication --------------------

    def vector_dot_product(self, other: "Vector") -> float:
        result = 0
        for index in range(self.size):
            result += self[index] * other[index]
        return result

    def scale(self, scalar: float) -> "Vector":
        return Vector([coord * scalar for coord in self.coordinates])

    def __mul__(
        self, other: Union["Vector", int, float]
    ) -> Union["Vector", float, int]:
        if isinstance(other, self.__class__):
            return self.vector_dot_product(other)

        elif isinstance(other, (int, float, complex)):
            return self.scale(other)

    # --------------- Printing -----------------------

    def print(self, title: str = "") -> Table:
        if title:
            print(
                Panel(
                    f"[bold]Vector - {title}[/bold]",
                    style="green",
                    expand=False,
                    border_style="dim white",
                )
            )
        tb = Table(style="dim cyan", show_header=False)
        tb.add_column()
        for coord in self.coordinates:
            tb.add_row(f"{coord:.2f}")

        print(tb)
        return tb

    def __str__(self):
        return f"{self.coordinates}"