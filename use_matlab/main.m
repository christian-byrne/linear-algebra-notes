v = Vector([1, 2, 3])
u = Vector([2, 1, 3])

product = v * u
projection = v.project(u)
orthogonalized = v.orthogonalize(u)
normal_vector = v.normal_vector()
direction_vector = v.direction_vector()
sum = v + u
difference = v - u
distance = v.distance_to(u)
