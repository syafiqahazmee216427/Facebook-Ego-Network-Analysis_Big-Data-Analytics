import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import community.community_louvain as community_louvain

# Task 2.2: Community Detection

import networkx as nx
import matplotlib.pyplot as plt
import community.community_louvain as community_louvain
from collections import Counter
import matplotlib.cm as cm

print("Community Detection")

# Louvain community detection
partition = community_louvain.best_partition(G)

# Number of communities
num_communities = len(set(partition.values()))
print("\nNumber of communities detected:", num_communities)

# Community sizes
community_sizes = Counter(partition.values())
print("Sizes of communities:", community_sizes)

# --- TOP NODES BY DEGREE CENTRALITY ---
top_n = 5
degree_centrality = nx.degree_centrality(G)
sorted_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

print("\nCommunity assignments for top Degree Centrality nodes:")
for node, centrality in sorted_nodes[:top_n]:
    community_id = partition[node]
    print(f"Node {node} is in community {community_id}")

# --- Visualization ---
pos = nx.spring_layout(G, seed=42)
fig = plt.figure(figsize=(10, 6))
fig.canvas.manager.set_window_title("Louvain Community Detection")

cmap = plt.get_cmap('viridis', num_communities)

for community_id in set(partition.values()):
    node_list = [node for node in partition if partition[node] == community_id]
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=node_list,
        node_size=30,
        node_color=[cmap(community_id)],
       
    )

nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='gray')
plt.title("Detected Communities in Graph (Louvain Method)")
plt.axis("off")

plt.show()
plt.figure(figsize=(8, 4))
communities = list(community_sizes.keys())
sizes = list(community_sizes.values())

# Graph Bar 
plt.bar(communities, sizes, color='skyblue')
plt.xlabel("Community ID")
plt.ylabel("Number of Nodes")
plt.title("Community Sizes")
plt.xticks(communities)  # Ensure all community IDs are shown
plt.tight_layout()
plt.show()
