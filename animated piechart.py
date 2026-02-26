import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

labels = ['Python', 'Java', 'C++', 'JavaScript']

fig, ax = plt.subplots()

def update(frame):
    ax.clear()  
    
    sizes = [random.randint(10, 50) for _ in range(4)]
    
    ax.pie(sizes,
           labels=labels,
           autopct='%1.1f%%',
           startangle=90)
    
    ax.set_title("Dynamic Programming Language Popularity")
ani = FuncAnimation(fig, update, interval=1000)

plt.show()
