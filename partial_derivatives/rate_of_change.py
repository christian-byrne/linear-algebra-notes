import math

# Define the function f(x, y) = x^2 + ln(y)
def f(x, y):
    return x**2 + math.log(y)

# Part (a): Average rate of change for z = f(x, y)
def average_rate_of_change_z(x1, y1, x2, y2):
    f1 = f(x1, y1)  # f at (x1, y1)
    f2 = f(x2, y2)  # f at (x2, y2)
    return (f2 - f1) / math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Change in z over distance

# Part (b): Partial derivatives (for directional derivative)
def partial_derivative_x(x, y):
    return 2 * x

def partial_derivative_y(x, y):
    return 1 / y

# Compute the directional derivative
def directional_derivative(x, y, dx, dy, magnitude):
    # Partial derivatives at (x, y)
    df_dx = partial_derivative_x(x, y)
    df_dy = partial_derivative_y(x, y)
    # Compute the directional derivative
    return (df_dx * (dx / magnitude)) + (df_dy * (dy / magnitude))

# Inputs
x1, y1 = 2, 1
x2, y2 = 3, 2

# Compute average rate of change in z
avg_rate_change_z = average_rate_of_change_z(x1, y1, x2, y2)

# Compute directional derivative for instantaneous rate of change
dx = x2 - x1
dy = y2 - y1
magnitude = math.sqrt(dx**2 + dy**2)
dir_derivative = directional_derivative(x1, y1, dx, dy, magnitude)

# Print results
def print_results_single_values():
    # Part (a)
    print(f"Average rate of change from (2, 1) to (3, 2): {round(avg_rate_change_z, 3)}")
    
    # Part (b)
    print(f"Instantaneous rate of change at (2, 1) heading towards (3, 2): {dir_derivative}")

# Call the function to print the results
print_results_single_values()
