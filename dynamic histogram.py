import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()

data = []

def update(frame):
    # Add new random value
    data.append(random.randint(1, 100))

    ax.clear()
    ax.hist(data, bins=10, color='orange', edgecolor='black')

    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

# Update every 1000 milliseconds (1 second)
ani = FuncAnimation(fig, update, interval=1000)

plt.show()
