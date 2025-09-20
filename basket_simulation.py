import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.patches import Rectangle

st.title("Projectile Motion Simulation / Basket Shot")

# User parameters
v0 = st.slider("Initial Velocity v0 (m/s)", 1, 30, 10)
angle = st.slider("Launch Angle (°)", 0, 90, 45)
g = st.slider("Gravity G (m/s²)", 1.0, 20.0, 9.81)

# =====================
# Fixed basket position
basket_x = 12  # fixed
basket_y = 3
basket_width = 1.0
basket_height = 0.5

# =====================
# Physics Model
# =====================
def projectile_motion(v0, angle_deg, g=9.81, dt=0.01):
    angle = np.radians(angle_deg)
    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)
    
    x_list = [0]
    y_list = [0]
    
    x = 0
    y = 0
    
    while y >= 0:
        x += vx * dt
        y += vy * dt
        vy -= g * dt
        x_list.append(x)
        y_list.append(y)
    
    return np.array(x_list), np.array(y_list)

x, y = projectile_motion(v0, angle, g)

# =====================
# Check basket hit (only if the ball is inside)
# =====================
hit = np.any((x >= basket_x) & (x <= basket_x + basket_width) &
             (y >= basket_y) & (y <= basket_y + basket_height))

if hit:
    st.success("Congratulations! You scored 🎯")
else:
    st.info("Oops! You missed the basket. Try again!")

# =====================
# Animation
# =====================
fig, ax = plt.subplots()
# Draw basket as a rectangle
basket_patch = Rectangle((basket_x, basket_y), basket_width, basket_height, color='orange')
ax.add_patch(basket_patch)

ax.set_xlim(0, max(x.max(), basket_x + basket_width)+1)
ax.set_ylim(0, max(y.max(), basket_y + basket_height)+1)
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_title("Projectile Motion")

line, = ax.plot([], [], 'bo-', lw=2)
placeholder = st.empty()

# Update animation every 3-5 points to speed it up
step = 5
for i in range(0, len(x), step):
    line.set_data(x[:i+1], y[:i+1])
    placeholder.pyplot(fig)

# Leave the final plot
placeholder.pyplot(fig)
