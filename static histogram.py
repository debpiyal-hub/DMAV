import matplotlib.pyplot as plt

# Sample data
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 
         40, 52, 67, 73, 88, 92, 58, 77, 84]

# Create histogram
plt.figure(figsize=(8,5))
plt.hist(marks, bins=5, color='skyblue', edgecolor='black')

# Add title and labels
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Show grid
plt.grid(axis='y')

# Display chart
plt.show()
