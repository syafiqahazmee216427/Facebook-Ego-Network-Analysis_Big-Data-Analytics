import networkx as nx

# Task 1.2: Choose and Load one ego-network into NetworkX
# Chosen ego-network: the edge list for ego user 0
# Load
def load_graph(path):
    G = nx.read_edgelist(path)
    return G
