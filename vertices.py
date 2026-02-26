import networkx as nx
import matplotlib.pyplot as plt

def create_complete_graph():
    try:
        # Take user input
        n = int(input("Enter number of vertices (greater than 3): "))

        if n <= 3:
            print("Number of vertices must be greater than 3.")
            return

        # Create complete graph
        G = nx.complete_graph(n)

        # Draw the graph
        plt.figure(figsize=(8, 8))
        pos = nx.circular_layout(G)  # Arrange nodes in circle
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="skyblue",
            node_size=2000,
            font_size=12,
            font_weight="bold",
            edge_color="gray"
        )

        plt.title(f"Complete Graph with {n} Vertices")
        plt.show()

        print(f"\nComplete Graph K{n} created successfully!")
        print(f"Number of nodes: {G.number_of_nodes()}")
        print(f"Number of edges: {G.number_of_edges()}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    create_complete_graph()
