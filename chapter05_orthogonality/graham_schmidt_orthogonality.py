from typing import List
from rich.table import Table
from rich.panel import Panel
from rich import print

from chapter01_vector.vector_class import Vector
from chapter01_vector.vector_batch import VectorBatch


class GrahamSchmidt:
    def __init__(self, vectors: List[Vector]):
        if isinstance(vectors, VectorBatch):
            self.vectors = vectors.vectors
        else:
            self.vectors = vectors

        self.orthogonal_vectors = VectorBatch()
        self.state = ""

    def reset(self):
        self.orthonormal_vectors = self.vectors[:]
        return self

    def orthogonalize(self) -> "GrahamSchmidt":
        if self.state == "orthogonal":
            return self

        self.orthogonal_vectors.clear()

        for index, vector in enumerate(self.vectors):
            if index == 0:
                self.orthogonal_vectors.append(vector)
            else:
                orthogonal_vector = vector.orthogonalize(
                    self.orthogonal_vectors[index - 1]
                )
                assert isinstance(orthogonal_vector, Vector)

                if orthogonal_vector.norm() == 0:
                    print(
                        f"Norm of orthogonal vector {orthogonal_vector.coordinates} is 0. Skipping"
                    )
                    continue

                orthogonal_vector.print("Created Orthogonal Vector")
                if orthogonal_vector not in self.orthogonal_vectors:
                    self.orthogonal_vectors.append(orthogonal_vector)

        self.state = "orthogonal"
        return self

    def orthnormalize(self) -> "GrahamSchmidt":
        if self.state != "orthogonal":
            self.orthogonalize()
        if self.state == "orthonormal":
            return self

        self.orthonormal_vectors = []
        for orthogonal_component in self.orthogonal_vectors:
            self.orthonormal_vectors.append(
                orthogonal_component * (1 / orthogonal_component.norm())
            )

        self.orthogonal_vectors = self.orthonormal_vectors[:]
        self.state = "orthonormal"
        return self

    def print(self, title: str = "") -> Table:
        if title:
            print(
                Panel(
                    f"[bold]Graham-Schmidt - {title}[/bold]",
                    style="green",
                    expand=False,
                    border_style="dim white",
                )
            )
        tb = Table(style="dim cyan", show_header=False)

        rows = self.orthogonal_vectors[0].size

        for i in range(len(self.orthogonal_vectors)):
            tb.add_column()

        for i in range(rows):
            tb.add_row(*[f"{v.coordinates[i]:.2f}" for v in self.orthogonal_vectors])

        print(tb)
        return self
