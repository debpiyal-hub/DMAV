import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 1000)
line, = ax.plot(x, np.sin(x))

ax.set_ylim(-2, 2)
ax.set_xlim(0, 2*np.pi)
ax.set_title("Animated Sine Wave")

# Animation function
def update(frame):
    y = np.sin(x + frame / 10)  # Shift wave
    line.set_ydata(y)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=50)

plt.show()