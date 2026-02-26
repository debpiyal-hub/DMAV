import matplotlib.pyplot as plt

# Enable interactive mode
plt.ion()

x_data = []
y1_data = []
y2_data = []

# Create figure with 2 subplots (2 rows, 1 column)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))

while True:
    user_input = input("Enter X, Y1, Y2 values separated by commas (or 'exit' to stop): ")

    if user_input.lower() == 'exit':
        break

    try:
        x_str, y1_str, y2_str = user_input.split(',')
        x = float(x_str.strip())
        y1 = float(y1_str.strip())
        y2 = float(y2_str.strip())

        # Append new data
        x_data.append(x)
        y1_data.append(y1)
        y2_data.append(y2)

        # Clear subplots
        ax1.cla()
        ax2.cla()

        # Plot on first subplot
        ax1.plot(x_data, y1_data, marker='o', color='blue')
        ax1.set_title("Y1 vs X")
        ax1.set_xlabel("X")
        ax1.set_ylabel("Y1")
        ax1.grid(True)

        # Plot on second subplot
        ax2.bar(x_data, y2_data, color='orange')
        ax2.set_title("Y2 vs X")
        ax2.set_xlabel("X")
        ax2.set_ylabel("Y2")
        ax2.grid(True)

        # Refresh figure
        plt.tight_layout()
        plt.pause(0.1)

    except ValueError:
        print("Invalid input! Please enter three numbers separated by commas.")

# Turn off interactive mode and show final plot
plt.ioff()
plt.show()
