# physics2
# simple_harmonic_oscillator.py
 
import numpy as np
import matplotlib.pyplot as plt

# System parameters
m = 1.0      # mass (kg)
k = 1.0      # spring constant (N/m)
x0 = 1.0     # initial position (m)
v0 = 0.0     # initial velocity (m/s)

# Simulation parameters
t_max = 10.0
dt = 0.01
t = np.arange(0, t_max, dt)   # time array

# Arrays for position and velocity
x = np.zeros_like(t)
v = np.zeros_like(t)

# Set initial conditions
x[0] = x0
v[0] = v0

# Time-stepping simulation using Euler method
for i in range(1, len(t)):
    a = -k/m * x[i-1]   # acceleration = -k/m * x
    v[i] = v[i-1] + a*dt
    x[i] = x[i-1] + v[i]*dt

# Plot the results
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Simple Harmonic Oscillator")
plt.grid(True)
plt.show()
