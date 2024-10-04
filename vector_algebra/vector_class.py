import math

from rich.table import Table
from rich import print
from rich.panel import Panel
from typing import List, Union, Tuple


class Vector:
    """
    **Vectors**: quantities that have both magnitude and direction.
    The word *vector* comes from the Latin word *vehere*, which means
    *to carry*. A vector is formed when a point is displaced — carried —
    a given distance in a given direction.

    The Point $A$ is called the *initial point* and the point $B$ is called the
    *terminal point*.

    Standard Position:
        A vector is in standard position if its initial point is at the origin.

    Notation:
        We can write a vector from point $A$ to point $B$ as [3, 2],
        where the first component is the $x$-component and the second component
        is the $y$-component.
        When vectors are referred to by their coordinates, they are being considered
        *analytically*.

    Vector Space Axioms:
        v + w = w + v
        (u + v) + w = u + (v + w)
        c(v + w) = cv + cw
        (c + d)v = cv + dv
        u + 0 = u for all vectors u.
        u + (-u) = 0 for all vectors u.
        1u = u for all vectors u.
        c(du) = (cd)u for all vectors u and all scalars c and d.

    """

    def __init__(self, coordinates: List[int]):
        self.coordinates = coordinates
        self.size = len(coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def normal_vector(self) -> "Vector":
        """
        Consider the line $l$ with equation $2x + y = 0$.
        The left-hand side of the equation can be seen as a dot product.
        I.e., $2x + y = [2, 1] \cdot [x, y]$.
        Then the equation becomes $n \cdot x = 0$, where $n = [2, 1]$.

        The vector $n$ is perpendicular to the line $l$ (since it describes a
        vector that goes from a point to 2 units to the right and 1 unit up -
        i.e., perpindicular to the slope of the line).
        In fact, it should be *orthogonal* to any vector that is parallel to
        the line $l$.

        Thus, if you take any point on the line $l$, $x$, and another point $p$,
        then the vector $\overrightarrow{px}$ is parallel to the line $l$ and
        equal to $x - p$.
        Thus, $n \cdot (x - p) = 0$.

        This vector $n$ is called the *normal vector* to the line $l$.
        The equation $n \cdot x = 0$ is called the *normal form* of the equation of
        the line $l$

        Returns:
            Vector: A normal vector to self.
        """
        if len(self.coordinates) != 2:
            raise ValueError(
                "Normal vector calculation is only supported for 2D vectors."
            )

        # Swap the components and negate one of them
        x, y = self.coordinates
        return Vector([-y, x])

    def direction(self) -> "Vector":
        """
        The direction vector of a vector is simply a unit vector (a vector
        with a magnitude of 1) that points in the same direction as the
        original vector.

        Formula:
            u = (a/||v||, b/||v||, c/||v||)

        Process:
            1. Calculate the magnitude (length) of `self`.
                ||`self`|| = √(a² + b² + c²), where a, b, c are components.
            2. Divide each component of `self` by magnitude.

        Returns:
            Vector: A new vector with the same direction as `self` but a
                magnitude of 1.

        """
        return self * (1 / self.norm())

    def distance_to_point(
        self, point_b: Tuple[Union[float, int, complex]]
    ) -> Union[float, int, complex]:
        """
        Refer to ![Picture Explanation](./pictures/projection-problem-1.png)

        Example from Textbook:
            We are given line_l through point_a = (3, 1, 1) with direction [-1, 1, 0].
            We find shortest distance to point_b = (1, 0, 2).
            See [Point to Line Function](./point_to_line.py).

            To translate this to a class method, instead of giving the point_a as (3, 1, 1),
            we should define this vector as [-1, 1, 0] through the point
            [3, 1, 2] - [1 * -1, 0 * 1, 2 * 0].
            I.e., point_a - vector through point_b with direction [-1, 1, 0].

        Args:
            point_b: An isolated point.

        Returns:
            float: The length of the vector from P to point_b, where P is the
                point on this vector that is closest to point_b.

        Process:
            1. Find `vector_self_to_b` from `self` to `point_b` by finding
                `vector_origin_to_b` and subtracting it from `self`.
            2. Find the `direction_vector` of `self`.
            2. Project `vector_self_to_b` onto our `direction_vector`.
            3. The difference between that projection and `vector_self_to_b` is the
                the vector from the closest point on line_l to point_b.
                It is the vector orthogonal to the projection of `vector_self_to_b`
                onto `direction_vector`.
            4. Return the length of that difference.

        """
        vector_origin_to_b = Vector(list(point_b))
        vector_self_to_b: Vector = vector_origin_to_b - self
        vector_self_to_b.print(
            "Vector from Head of Self → (Head of Vector from Origin → point_b)"
        )

        self_direction = self.direction()
        self_direction.print("Direction Vector for Self")

        vector_self_to_p = vector_self_to_b.project(self)
        vector_self_to_p.print("Vector from Self Tail -> Point P")

        distance_vector: Vector = vector_self_to_b - vector_self_to_p
        distance = distance_vector.norm()
        print(
            f"Length of the vector from P to point_b, where P is the point on self that is closest to point_b:\n{distance}"
        )

        return distance

    def distance_to_other_vector(self, other: "Vector") -> Union[float, int, complex]:
        """
        The distance between vectors is a direct analogue to the distance
        between points in space.

        Formula:
            Given two vectors $u$ and $v$, the distance between them is the
            length/norm of the vector that connects the two vectors, $u - v$.

        Example from Book:
            u = [sqrt(2), 1, -1]
            v = [0, 2, -2]
            distance(u, v) = 2

        Source:
            [Source](../chapter01_vector/distance-and-angles.md)

        """
        # It is not necessary to use absolute value because the components will be squared.
        difference: "Vector" = other - self
        return difference.norm()

    def distance_to(
        self, other: Union["Vector", Tuple[Union[float, int, complex]]]
    ) -> Union[float, int, complex]:
        """See documentation for `distance_to_other_vector` and `distance_to_point`"""
        if isinstance(other, Vector):
            return self.distance_to_other_vector(other)
        elif isinstance(other, tuple):
            return self.distance_to_point(other)

    def angle_from(self, other: "Vector") -> float:
        """
        In $R^2$ and $R^3$, the angle between the nonzero vectors $u$ and $v$
        will refer to the angle $\theta$ such that $0 \leq \theta \leq \pi$ or
        $0 \leq \theta \leq 180^\circ$

        Formula:
            $\cos(\theta) = \frac{u \cdot v}{\|u\| \|v\|}$

        Example from Book:
            u = [2, 1, -2]
            v = [1, 1, 1]
            angle between = 78.9°

        Source:
            [Source](../chapter01_vector/distance-and-angles.md)

        """
        theta = (self * other) / (self.norm() * other.norm())
        return math.cos(theta)

    def is_zero_vector(self) -> bool:
        """
        The zero vector is the vector that has no magnitude and no direction.
        It is denoted by $\overrightarrow{0}$.

        To check if this `Vector` instance is the zero vector, check if all
        its components are zero.
        """
        return all([coord == 0 for coord in self.coordinates])

    def norm(self) -> Union[float, int, complex]:
        """
        In $R^2$, the length of a vector is the distance from the origin to the
        point $(x, y)$ which by Pythagorean theorem is $\sqrt{x^2 + y^2}$.

        **Length** (or **norm**): The length of a vector $v$ is denoted by
        $\|v\|$ and is defined as $\|v\| = \sqrt{v \cdot v} =
        \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}$.

        I.e., the length of a vector is the square root of the sum of the squares
        of its components.

        Can be rewritten to show: $\|v\|^2 = v \cdot v = v_1^2 + v_2^2 + \ldots + v_n^2$.

        Properties:
            **Non-negativity**: $\|v\| \geq 0$ and $\|v\| = 0$ if and only if $v = 0$.
            **Homogeneity**: $\|\alpha v\| = |\alpha| \|v\|$ for any scalar $\alpha$.

        Unit Vectors
            A **unit vector** is a vector of length 1.
            In $R^2$, the unit vector in the direction of a vector $v$ is $\frac{v}{\|v\|}$.

        Standard Unit Vectors:
            In general, in $R^n$, we define unit vectors $e_1, e_2, \ldots, e_n$ as follows:
                $e_1 = [1, 0, 0, \ldots, 0]$
                $e_2 = [0, 1, 0, \ldots, 0]$
                $\ldots$
                $e_n = [0, 0, 0, \ldots, 1]$
            These vectors are called the **standard unit vectors** in $R^n$.
            They form a basis for $R^n$.

        """
        return sum([coord**2 for coord in self.coordinates]) ** (1 / 2)

    def project(self, onto: "Vector") -> "Vector":
        """
        The term *projection* comes from the idea of projecting an image onto a wall.
        Imagine a beam of light ways rays parallel to each other and perpendicular
        to the $u$ shining down on $v$. The projection of $v$ onto $u$ is just the
        shadow cast, or projected, by $v$ onto $u$.

        Obtuse Angles:
            If the angle between $u$ and $v$ is obtuse, then the projection of
            $v$ onto $u$ will be negative. This is because the projection is the
            length of the shadow cast by $v$ onto $u$, and if the angle is obtuse,
            the shadow will be cast in the opposite direction of $u$.

        With Unit Vectors:
            If $u$ is a unit vector, then the projection of $v$ onto $u$ is just the
            scalar projection of $v$ onto $u$.
            I.e., $\text{proj}_u v = (u \cdot v)u$

        Process:
            1. Define a vector $p$ to represent the projection such that it has the
               direction of `onto` but terminates at the vector orthogonal to `onto`
               with head at `onto` and tail at `self`.
            2. From trig, we know that $cos(\theta) = \frac{adjacent}{hypotenuse} =
               \frac{||p||}{||`self`||}$
            3. Solve for $||p||$: $||p|| = ||v||cos(\theta)$
            4. Since $p = ||p||\frac{u}{||u||}u$, we can substitute $||p||$ to get
               $p = ||v||cos(\theta)\frac{u}{||u||}u$
            5. From the formula for angle difference between vectors:
               cos(\theta) = \frac{u \cdot v}{||u|| \cdot ||v||}$
            6. Substitute: $p = ||v|| \frac{u \cdot v}{||u|| \cdot ||v||} \frac{1}{||u||}u$
            7. Cancel out the $||v||$ terms to get $p = \frac{u \cdot v}{||u||} \frac{1}{||u||}u$
            8. We know that $||u|| ||u|| = u \cdot u$
               (since $u \cdot u = ||u||^2$),
               so we can substitute that in to get
               $p = \frac{u \cdot v}{u \cdot u}u$
            9. Thus, the vector $p$ is given by $p = \frac{u \cdot v}{u \cdot u}u$

        """
        coefficient = (self * onto) / (onto * onto)
        return onto.scalar_multiply(coefficient)

    def is_orthogonal_to(self, other_vector: "Vector") -> bool:
        """
        You can generalize the idea of perpindicularity to vectors in $R^n$,
        where it is called **orthogonality**.

        > The word orthogonal is derived from the Greek words orthos, meaning
        > “upright,” and gonia, meaning “angle.” Hence, orthogonal literally
        > means “right-angled.”

        Formula:
            In $R^2$ or $R^3$, two vectors are orthogonal if their dot product is zero.
            I.e., the angle between the two vectors is $90^\circ$ or $\frac{\pi}{2}$.
            Thus, $\frac{u \cdot v}{\|u\| \|v\|} = \cos(\frac{\pi}{2}) = 0$.

        Zero Vector Orthogonality:
            Since $0 \cdot v = 0$ for any vector $v$, the zero vector is orthogonal to every vector.

        Pythagoras' Theorem

            In $R^2$ or $R^3$, if two vectors are orthogonal, then the magnitude of
            the sum of the vectors is the square root of the sum of the squares of
            the magnitudes of the vectors.
            I.e., if $u \cdot v = 0$, then $\|u + v\|^2 = \|u\|^2 + \|v\|^2$.
            This is a generalization of Pythagoras' theorem to vectors in $R^n$.

        """
        return (
            # Check if either is zero vector.
            any([self.is_zero_vector(), other_vector.is_zero_vector()])
            # If not, check if their dot product is 0.
            or self * other_vector == 0
        )

    def orthogonalize(self, onto: "Vector") -> "Vector":
        projection = self.project(onto)
        return self - projection

    def __len__(self):
        return self.size

    # ------------- Operations ---------------

    def __eq__(self, other: "Vector") -> bool:
        """
        Two vectors are equal if they have the same magnitude and direction.

        Every vector can be redrawn so that it is in standard position.
        This is called the *equivalent vector*.
        """
        if isinstance(other, list):
            other_coords = other
        else:
            other_coords = other.coordinates
        return self.coordinates == other_coords

    def __add__(self, other: Union["Vector", float, int, complex]) -> "Vector":
        """
        The sum of two vectors $\overrightarrow{v}$ and $\overrightarrow{w}$ is
        the vector that results from placing the initial point of
        $\overrightarrow{w}$ at the terminal point of $\overrightarrow{v}$.

        $u + v = [u_1 + v_1, u_2 + v_2]$

        The Parallelogram Law:
            The sum of two vectors is the diagonal of the parallelogram formed by the two vectors.
            ![Picture](pictures/parallelogram-rule.png)

        """
        if isinstance(other, self.__class__):
            return Vector(
                [
                    coord1 + coord2
                    for coord1, coord2 in zip(self.coordinates, other.coordinates)
                ]
            )
        else:
            return Vector([coord + other for coord in self.coordinates])

    def __sub__(self, other: "Vector") -> "Vector":
        """
        The difference of two vectors $\overrightarrow{v}$ and $\overrightarrow{w}$
        is the vector that results from placing the initial point of
        $\overrightarrow{w}$ at the terminal point of $\overrightarrow{v}$ and then
        reversing the direction of $\overrightarrow{w}$.

        $u - v$ corresponds to the "other" diagonal of the parallelogram formed by $u$ and $v$.

        """
        return Vector(
            [
                coord1 - coord2
                for coord1, coord2 in zip(self.coordinates, other.coordinates)
            ]
        )

    def dot_product(self, other: "Vector") -> float:
        """
        The dot product of two vectors $\overrightarrow{v}$ and $\overrightarrow{w}$
        is the scalar that results from multiplying the corresponding components of
        $\overrightarrow{v}$ and $\overrightarrow{w}$ and then adding the products.

        The dot product of vectors in $R^n$ is a special and important case of the more general notion of **inner product**

        Teminology:
            Since the return value is a number (not a vector), $u \cdot v$ is sometimes
            called the **scalar product** of $u$ and $v$.

        Inner Product Properties:
            $u \cdot v = v \cdot u$
            $u \cdot (v + w) = u \cdot v + u \cdot w$
            $(c + d)u \cdot v = cu \cdot v + du \cdot v$
            $u \cdot u \geq 0$ and $u \cdot u = 0$ if and only if $u = 0$.
            $(cu) \cdot v = c(u \cdot v)$

        """
        result = 0
        for index in range(self.size):
            result += self[index] * other[index]
        return result

    def scalar_multiply(self, scalar: float) -> "Vector":
        """
        The product of a scalar $c$ and a vector $\overrightarrow{v}$ is the vector
        that results from multiplying each component of $\overrightarrow{v}$ by
        $c$, or the magnitude of $\overrightarrow{v}$ by $c$.

        $cv$ is $|c|$ times as long as $v$.

        Direction:
            $cv$ has the same direction as $v$ if $c > 0$ and the opposite direction if $c < 0$.

        Teminology:
            $cv$ is a "scaled" version of $v$.
            Two vectors are **scalar multiples** of each other if and only if they are parallel.

        """
        return Vector([coord * scalar for coord in self.coordinates])

    def __mul__(
        self, other: Union["Vector", int, float]
    ) -> Union["Vector", float, int]:
        # If multiply two vectors, assume dot product.
        if isinstance(other, self.__class__):
            return self.dot_product(other)

        # If multiply by a number, assume scalar multiplication.
        elif isinstance(other, (int, float, complex)):
            return self.scalar_multiply(other)

    # --------------- Printing -----------------------

    def print(self, title: str = "") -> Table:
        if title:
            print(
                Panel(
                    f"[bold]Vector - {title}[/bold]".replace("->", "→"),
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
