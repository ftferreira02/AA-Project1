import networkx as nx
import numpy as np
import random
import math
import pickle
from itertools import combinations
import matplotlib.pyplot as plt  # For graph visualization
import os

# Seed for reproducibility (use your student number)
random.seed(124467)

# Define the directory to save the graphs
GRAPH_DIR = "Graphs"

# Ensure the directory exists
os.makedirs(GRAPH_DIR, exist_ok=True)

def generate_vertex_coordinates(num_vertices, min_distance=10, coordinate_range=(1, 1000)):
    """Generate distinct vertex coordinates in 2D space with minimum distance constraints."""
    coordinates = []
    while len(coordinates) < num_vertices:
        x, y = random.randint(*coordinate_range), random.randint(*coordinate_range)
        # Ensure the point is not too close to any existing point
        if all(math.dist((x, y), coord) >= min_distance for coord in coordinates):
            coordinates.append((x, y))
    return coordinates

def create_graph_with_density(num_vertices, density, min_distance=10):
    """Create a graph with a specified number of vertices and edge density."""
    # Step 1: Generate vertices with distinct coordinates
    coordinates = generate_vertex_coordinates(num_vertices, min_distance)
    
    # Step 2: Initialize the graph and add nodes with coordinates as attributes
    G = nx.Graph()
    for idx, coord in enumerate(coordinates):
        G.add_node(idx, pos=coord)
    
    # Step 3: Create all possible edges between pairs of nodes
    possible_edges = list(combinations(range(num_vertices), 2))
    max_edges = len(possible_edges)
    
    # Step 4: Calculate number of edges based on density
    num_edges = int(density * max_edges)
    
    # Step 5: Randomly sample edges to add to the graph
    edges_to_add = random.sample(possible_edges, num_edges)
    G.add_edges_from(edges_to_add)
    
    return G

def save_graph(graph, filename):
    """Save the graph instance to a specified directory using pickle."""
    filepath = os.path.join(GRAPH_DIR, filename)
    with open(filepath, 'wb') as f:
        pickle.dump(graph, f)
    print(f"Graph saved as: {filepath}")

def load_graph(filename):
    """Load a graph from the specified directory."""
    filepath = os.path.join(GRAPH_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            graph = pickle.load(f)
        return graph
    else:
        print(f"File '{filename}' not found in directory '{GRAPH_DIR}'.")
        return None
    
def visualize_graph(graph):
    """Visualize the graph using Matplotlib."""
    pos = nx.get_node_attributes(graph, 'pos')  # Get node positions
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

def main():
    choice = input("Do you want to (1) create new graphs or (2) load and view an existing graph? Enter 1 or 2: ")
    
    if choice == '1':
        densities = [0.125, 0.25, 0.5, 0.75]
        max_vertices = 10

        for num_vertices in range(4, max_vertices + 1):
            for density in densities:
                G = create_graph_with_density(num_vertices, density)
                
                filename = f"graph_{num_vertices}_vertices_{int(density*100)}pct_edges.pkl"
                save_graph(G, filename)

    elif choice == '2':
        print(f"Available files in '{GRAPH_DIR}':")
        files = os.listdir(GRAPH_DIR)
        pkl_files = [f for f in files if f.endswith('.pkl')]
        
        if pkl_files:
            for i, file in enumerate(pkl_files, start=1):
                print(f"{i}. {file}")
            file_choice = int(input("Enter the number of the file you want to load: ")) - 1
            
            if 0 <= file_choice < len(pkl_files):
                filename = pkl_files[file_choice]
                G = load_graph(filename)
                if G:
                    print(f"Loaded graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
                    visualize_graph(G)
            else:
                print("Invalid selection.")
        else:
            print("No pickle files found in the directory.")

if __name__ == "__main__":
    main()
