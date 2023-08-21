import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model (differential equation)
def model(y, t, k):
    dx_dt = rho * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - x * y_1 - beta * z
    dy1_dt = x * z - 2 * x * z_1 - d_0 * y_1
    dz1_dt = 2 * x * y_1 - 4 * beta * z_1
    return dydt

# Initial condition
y0 = 1

# Time points at which solution is to be computed
t = np.linspace(0, 10, 100)

# Growth constant
k = 1.0

# Solve ODE
y = odeint(model, y0, t, args=(k,))

# Plot results
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Exponential Growth')
plt.grid(True)
plt.show()