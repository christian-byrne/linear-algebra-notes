import numpy as np
from scipy.integrate import quad

def integrand(x, equation):
    """
    Integrand function that takes x as the variable and evaluates the equation.
    """
    return equation(x, np.sqrt(1 - x**2))  # y = sqrt(1 - x^2) on the unit circle

def integrate_unit_circle(equation, upper_half=True, lower_half=False, left_half=False, right_half=True, **kwargs):
    """
    Integrates the given equation over the unit circle with optional limits.
    
    Parameters:
        equation (function): A function of x and y (the equation to integrate).
        upper_half (bool): If True, integrates over the upper half of the circle.
        lower_half (bool): If True, integrates over the lower half of the circle.
        left_half (bool): If True, integrates over the left half of the circle.
        right_half (bool): If True, integrates over the right half of the circle.
        
    Returns:
        result (float): The result of the integration.
    """
    result = 0
    
    # Define integration ranges for different circle parts
    if upper_half:
        # Upper half corresponds to x in [-1, 1], y = sqrt(1 - x^2) >= 0
        res, _ = quad(lambda x: integrand(x, equation), -1, 1, **kwargs)
        result += res
    
    if lower_half:
        # Lower half corresponds to x in [-1, 1], y = -sqrt(1 - x^2)
        res, _ = quad(lambda x: integrand(x, lambda x, y: equation(x, -y)), -1, 1, **kwargs)
        result += res
    
    if left_half:
        # Left half corresponds to y in [-1, 1], x = -sqrt(1 - y^2)
        res, _ = quad(lambda y: integrand(-np.sqrt(1 - y**2), equation), -1, 1, **kwargs)
        result += res
    
    if right_half:
        # Right half corresponds to y in [-1, 1], x = sqrt(1 - y^2)
        res, _ = quad(lambda y: integrand(np.sqrt(1 - y**2), equation), -1, 1, **kwargs)
        result += res

    return result

# Example usage:
# Define the equation as a function of x and y
# equation = lambda x, y: x**2 + y**2
# equation = lambda x, y: x * np.e**(-x**2)
# equation = lambda x, y: x**4 * y**2
# equation = lambda x, y: y * np.e**(-y)
equation = lambda x, y: (y + 10)

# Integrate over the upper half of the unit circle
result = integrate_unit_circle(equation, upper_half=False, lower_half=True, left_half=True, right_half=False)
print(f"Result of integration: {result}")
