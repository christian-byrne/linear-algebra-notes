import math

# Define the function f(x, y) = e^(-x) * sin(y)
def f(x, y):
    return math.exp(-x) * math.sin(y)

# Function to compute the partial derivative with respect to x using difference quotient
def partial_x(x, y, delta_x):
    return (f(x + delta_x, y) - f(x, y)) / delta_x

# Function to compute the partial derivative with respect to y using difference quotient
def partial_y(x, y, delta_y):
    return (f(x, y + delta_y) - f(x, y)) / delta_y

def main():
    # Ask user whether they want to test for x or y
    test_variable = input("Do you want to test for x or y? (Enter 'x' or 'y'): ").strip().lower()

    # Input delta value
    delta = float(input("Enter the delta value (e.g., 0.1): "))

    # Define the point (x, y)
    x = 1
    y = 8

    # Compute and print the partial derivative
    if test_variable == 'x':
        result = partial_x(x, y, delta)
        print(f"Partial derivative with respect to x at (1, 8) with delta {delta} is: {round(result, 4)}")
    elif test_variable == 'y':
        result = partial_y(x, y, delta)
        print(f"Partial derivative with respect to y at (1, 8) with delta {delta} is: {round(result, 4)}")
    else:
        print("Invalid input! Please enter 'x' or 'y'.")

if __name__ == "__main__":
    main()

