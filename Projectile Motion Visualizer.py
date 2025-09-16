import numpy as np
import matplotlib.pyplot as plt
 
# Constants
g = 9.81  # gravity (m/s^2)

# User input
v0 = float(input("Initial velocity (m/s): "))
angle_deg = float(input("Launch angle (degrees): "))

# Convert angle to radians
angle_rad = np.radians(angle_deg)

# Time of flight
t_flight = 2 * v0 * np.sin(angle_rad) / g

# Time points
t = np.linspace(0, t_flight, num=100)

# Trajectory
x = v0 * np.cos(angle_rad) * t
y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

# Maximum height
max_height = (v0**2 * np.sin(angle_rad)**2) / (2 * g)
print(f"Maximum height: {max_height:.2f} m")

# Plot trajectory
plt.plot(x, y, label=f"v0={v0} m/s, angle={angle_deg}°")
plt.title("Projectile Motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.legend()
plt.grid()
plt.show()
