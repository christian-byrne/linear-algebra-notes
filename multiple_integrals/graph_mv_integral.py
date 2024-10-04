import numpy as np
import matplotlib.pyplot as plt

# Define the limits of integration
def y1(x):
    return np.cos(np.pi * x)

def y2(x):
    return x - 2

# Generate x values for plotting
x_vals = np.linspace(0, 1, 100)

# Plot the region of integration
plt.fill_between(x_vals, y1(x_vals), y2(x_vals), color='lightblue', label='Region of Integration')
plt.plot(x_vals, y1(x_vals), label='y = cos(pi * x)', color='blue')
plt.plot(x_vals, y2(x_vals), label='y = x - 2', color='red')

# Labels and display
plt.xlabel('x')
plt.ylabel('y')
plt.title('Region of Integration')
plt.legend()
plt.grid(True)
plt.show()
