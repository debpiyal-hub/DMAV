import matplotlib.pyplot as plt

# Enable interactive mode
plt.ion()

x_data = []
y_data = []

plt.figure(figsize=(8,5))
plt.title("Dynamic Scatter Plot (User Input)")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.grid(True)

while True:
    user_input = input("Enter X and Y values separated by a comma (or type 'exit' to stop): ")

    if user_input.lower() == 'exit':
        break

    try:
        x_str, y_str = user_input.split(',')
        x = float(x_str.strip())
        y = float(y_str.strip())

        x_data.append(x)
        y_data.append(y)

        plt.clf()  # Clear previous points
        plt.scatter(x_data, y_data, color='blue')
        plt.title("Dynamic Scatter Plot (User Input)")
        plt.xlabel("X Value")
        plt.ylabel("Y Value")
        plt.grid(True)
        plt.pause(0.1)  # Pause to update the plot

    except ValueError:
        print("Invalid input! Please enter two numbers separated by a comma.")

plt.ioff()
plt.show()
