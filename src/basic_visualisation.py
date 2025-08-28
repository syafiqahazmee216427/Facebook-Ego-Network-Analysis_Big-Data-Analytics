import networkx as nx
import matplotlib.pyplot as plt

# Basic visualization of the network
# Draw the graph

# Use a spring layout for clearer spacing
pos = nx.spring_layout(G, seed=42)  # reproducible layout

# Create the figure
fig = plt.figure(figsize=(10, 6))

# Set the figure window title
fig.canvas.manager.set_window_title("Facebook Ego Network – User 0")

nx.draw(
    G,
    pos,
    node_size=30,
    edge_color="orange",
    with_labels=False,
    alpha=0.6
)
plt.title("Facebook Ego Network – User 0 (Spring Layout)")
plt.savefig("results/basic_visualisation.png", dpi=300, bbox_inches="tight")
plt.show()
