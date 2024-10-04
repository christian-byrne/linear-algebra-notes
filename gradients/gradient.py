import numpy as np

def f_x(x, y):
    return 3 * x**2 * np.log(1 + y**2)

def f_y(x, y, z):
    return (2 * x * y) / (1 + y**2) - z * np.sin(y * z)

def f_z(y, z):
    return y * np.sin(y * z)

def gradient(x, y, z):
    grad_x = f_x(x, y)
    grad_y = f_y(x, y, z)
    grad_z = f_z(y, z)
    return np.array([grad_x, grad_y, grad_z])

def normalize(v):
    norm = np.linalg.norm(v)
    return v / norm

# Given point (x, y, z)
point = np.array([2, 1, -np.pi/2])

# Compute gradient at the given point
grad_at_point = gradient(point[0], point[1], point[2])

# Given direction vector ⟨2, -11, 10⟩
direction = np.array([2, -11, 10])
direction_normalized = normalize(direction)

# Directional derivative
directional_derivative = np.dot(grad_at_point, direction_normalized)

# Vector of greatest decrease
greatest_decrease = -grad_at_point

# Output results
print("Gradient at the point:", grad_at_point)
print("Normalized direction vector:", direction_normalized)
print("Directional derivative:", directional_derivative)
print("Vector of greatest decrease:", greatest_decrease)
