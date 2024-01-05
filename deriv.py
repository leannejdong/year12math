import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**2

def derivative(x):
    return 2 * x

# Generate x values
x_values = np.linspace(-5, 5, 100)

# Calculate y values for the function and its derivative
y_function = function(x_values)
y_derivative = derivative(x_values)

# Plot the function
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x_values, y_function, label='f(x) = x^2')
plt.title('Function: f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Plot the derivative
plt.subplot(1, 2, 2)
plt.plot(x_values, y_derivative, label="f'(x) = 2x")
plt.title("Derivative: f'(x) = 2x")
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
