import matplotlib.pyplot as plt

# Enable interactive mode
plt.ion()

x_data = []
y_data = []

plt.figure(figsize=(8,5))

count = 1

while True:
    user_input = input("Enter a value (or type 'exit' to stop): ")

    if user_input.lower() == 'exit':
        break

    try:
        value = float(user_input)

        x_data.append(count)
        y_data.append(value)
        count += 1

        plt.clf()  # Clear figure
        plt.plot(x_data, y_data, marker='o', color='blue')
        plt.title("Dynamic Line Chart (User Input)")
        plt.xlabel("Entry Number")
        plt.ylabel("Value")
        plt.grid(True)

        plt.pause(0.1)

    except ValueError:
        print("Please enter a valid number.")

plt.ioff()
plt.show()
