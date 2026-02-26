import matplotlib.pyplot as plt

# Sample data
x = [1, 3, 5, 7, 9, 8]
y1 = [10, 14, 19, 24, 30, 35]
y2 = [35, 30, 28, 20, 15, 10]

# Create subplots (2 rows, 1 column)
fig, axs = plt.subplots(2, 1, figsize=(8,8))

# First subplot
axs[0].plot(x, y1, color='blue', marker='o')
axs[0].set_title("Line Plot 1")
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")
axs[0].grid(True)

# Second subplot
axs[1].bar(x, y2, color='orange')
axs[1].set_title("Bar Plot 2")
axs[1].set_xlabel("X-axis")
axs[1].set_ylabel("Y-axis")
axs[1].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()
