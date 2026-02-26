import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots(figsize=(8,5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.grid(True)

# Create a circle
circle = patches.Circle((0, 2.5), radius=0.3, color='blue')
ax.add_patch(circle)

# Animation update function
def update(frame):
    x = frame / 10  # Move circle horizontally
    circle.center = (x % 10, 2.5)  # Wrap around when reaching edge
    return circle,

# Create animation
ani = FuncAnimation(fig, update, frames=range(0, 200), interval=50, blit=True)

plt.show()
