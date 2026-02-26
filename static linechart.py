import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 180, 220, 250, 300]

plt.figure(figsize=(8,5))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')

plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.grid(True)

plt.show()
