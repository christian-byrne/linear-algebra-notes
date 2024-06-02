from chapter01_vector.vector_class import Vector
from typing import Tuple, Union

def distance_point_to_line(
    point_a: Tuple[Union[float, int, complex]],
    point_b: Tuple[Union[float, int, complex]],
    direction_vector: Vector,
):
    """
    Refer to ![Picture Explanation](./pictures/projection-problem-1.png)
    
    Args:
      point_b: An isolated point.
      point_a: A point on the line_l.
      direction_vector: The direction vector for line_l.

    Returns:
      float: The length of the vector PB, where P is the point on line_l 
        that is closest to point_b. 

    Process:
      1. Consider point_a and point_b as vectors from the origin, then 
         calculate their difference to find the vector between them, 
         termed `vector_ab`
      2. Project `vector_ab` onto the `direction_vector` of line_l.
      3. The difference between that projection and `vector_ab` is the
         the vector from the closest point on line_l to point_b.
         It is the vector orthogonal to the projection of `vector_ab`
         onto `direction_vector`.
      4. Normalize that vector to find the length.

    """
    # Step 1: Define the vector from point_a to point_b.

    # Define them as vectors from the origin.
    vector_a = Vector(list(point_a))  # Vector from origin to point_a
    vector_b = Vector(list(point_b))  # Vector from origin to point_b

    # The difference between vector_b and vector_a is equivalent to the 
    # vector from point_a to point_b.
    vector_ab = vector_b - vector_a
    vector_ab.print("vector_ab")

    # Step 2: Project vector_ab onto the direction_vector to get the 
    # vector from point_a to P.
    vector_ap = vector_ab.project(direction_vector)
    vector_ap.print("vector_ap")

    # Step 3: Find the difference between the projected vector and vector_ab
    distance_vector: Vector = vector_ab - vector_ap
    distance_vector.print("distance_vector from vector_ab to vector_ap")

    # Step 4: Normalize
    distance = distance_vector.norm()

    return distance 
