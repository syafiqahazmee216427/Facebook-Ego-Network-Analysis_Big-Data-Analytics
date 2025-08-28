import networkx as nx

# Basic Graph Properties
print(f"Graph info:")

# Number of nodes
num_nodes = G.number_of_nodes()
print("Number of nodes:", num_nodes)

# Number of edges
num_edges = G.number_of_edges()
print("Number of edges:", num_edges)

# Graph density
density = nx.density(G)
print("Graph density:", round(density, 4))

# View some nodes and edges
print()
print("Sample nodes:", list(G.nodes())[:5])
print("Sample edges:", list(G.edges())[:5])

# Check if the graph is connected
is_connected = nx.is_connected(G)
print()
print("Is the graph connected?", is_connected)

# If not connected, find number of connected components
if not is_connected:
    components = list(nx.connected_components(G))
    print("Number of connected components:", len(components))

    # Optionally print size of the largest component
    largest_component = max(components, key=len)
    print("Size of largest component:", len(largest_component))
