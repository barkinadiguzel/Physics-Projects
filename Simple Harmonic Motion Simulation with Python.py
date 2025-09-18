import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Parameters
A = 1       # Amplitude (meters)
k = 10      # Spring constant (N/m)
m = 0.5     # Mass (kg)
omega = np.sqrt(k/m)  # Angular frequency
t_max = 10  # Simulation time (seconds)
dt = 0.02   # Time step

# Time array and position
t = np.arange(0, t_max, dt)
x = A * np.cos(omega * t)  # Position as a function of time

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-A-0.2, A+0.2)
ax.set_ylim(-0.5, 0.5)
ax.set_title("Simple Harmonic Motion")
ax.set_xlabel("Position (m)")
ax.set_yticks([])  # Hide y-axis ticks

# Point representing the ball
ball, = ax.plot([], [], 'bo', markersize=20)

# Update function for animation
def update(frame):
    ball.set_data([x[frame]], [0])  # Update x position
    return ball,

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=dt*1000, blit=True)

plt.show()
