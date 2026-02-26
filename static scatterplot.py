import matplotlib.pyplot as plt

# Sample data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
marks_scored = [35, 40, 50, 55, 65, 70, 80, 90]

# Create scatter plot
plt.figure(figsize=(8,5))
plt.scatter(hours_studied, marks_scored, color='red', marker='o')

# Add title and labels
plt.title("Hours Studied vs Marks Scored")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")

# Show grid
plt.grid(True)

# Display plot
plt.show()
