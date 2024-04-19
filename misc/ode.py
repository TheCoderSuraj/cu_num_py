import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define a simple ODE (dy/dt = y)
def linear_model(y, t):
    dydt = y + 1
    return dydt

# Initial condition
y0 = 2

# Time points
t = np.linspace(0, 10, 100)

# Solve the ODE
solution = odeint(linear_model, y0, t)

# Plot the results
plt.plot(t, solution)
plt.xlabel('Time')
plt.ylabel('y')
plt.title('Solution of dy/dt = y')
plt.show()
