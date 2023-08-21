import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model (differential equation)
def model(Y, t, a, b, c, d, e, f):
    x, y, z = Y

    dx_dt = a * (y - x) + d * x * z
    dy_dt = b * x - x * z + f * y
    dz_dt = c * z + x * y - e * x * x
    return [dx_dt, dy_dt, dz_dt]

# Parameters
a = 32.48
b = 45.84
c = 1.18
d = 0.13
e = 0.57
f = 14.7

# Initial condition
x0 = -0.29
y0 = -0.25
z0 = -0.59

# Time points at which solution is to be computed
t = np.linspace(0, 5, 50000)

# Growth constant

# Integrate the differential equations
sol = odeint(model, [x0, y0, z0], t, args=(a, b, c, d, e, f))

# Plot the solution
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol[:, 0], sol[:, 1], sol[:, 2])
ax.set_title('Chaos System')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()