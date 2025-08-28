import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Centrality Calculation

# === DEGREE CENTRALITY ===
degree_centrality = nx.degree_centrality(G)
top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 by Degree Centrality:")
for node, score in top_degree:
    print(f"Node {node}: {score:.4f}")

# Visualization
fig, ax = plt.subplots(figsize=(10, 7))
fig.suptitle("Facebook Ego-Network: Degree Centrality Visualization", fontsize=14)

node_color = [degree_centrality[node] for node in G.nodes()]
node_size = [5000 * degree_centrality[node] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_size, node_color=node_color, cmap=plt.cm.Blues, alpha=0.8)
nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.3)
top_5_nodes = [node for node, _ in top_degree]
nx.draw_networkx_labels(G, pos, labels={node: node for node in top_5_nodes}, font_size=10, font_color='black', ax=ax)

sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(node_color), vmax=max(node_color)))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label("Degree Centrality")

ax.axis("off")
plt.tight_layout()
plt.show()

# Bar Plot
top5_degree_df = pd.DataFrame(top_degree, columns=["Node", "Degree Centrality"])
fig, ax = plt.subplots(figsize=(8, 4))
norm = plt.Normalize(vmin=min(top5_degree_df["Degree Centrality"]), vmax=max(top5_degree_df["Degree Centrality"]))
colors = [plt.cm.Blues(norm(val)) for val in top5_degree_df["Degree Centrality"]]

sns.barplot(data=top5_degree_df, x="Degree Centrality", y="Node", palette=colors, ax=ax)
plt.title("Top 5 Users by Degree Centrality", fontsize=13)
for i, (node, centrality) in enumerate(top_degree):
    ax.text(centrality + 0.002, i, f"{centrality:.4f}", va='center')
sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label("Degree Centrality")
plt.tight_layout()
plt.show()

# === BETWEENNESS CENTRALITY ===
betweenness_centrality = nx.betweenness_centrality(G)
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 by Betweenness Centrality:")
for node, score in top_betweenness:
    print(f"Node {node}: {score:.4f}")

fig, ax = plt.subplots(figsize=(10, 7))
fig.suptitle("Facebook Ego-Network: Betweenness Centrality Visualization", fontsize=14)

node_color = [betweenness_centrality[node] for node in G.nodes()]
node_size = [5000 * betweenness_centrality[node] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_size, node_color=node_color, cmap=plt.cm.Greens, alpha=0.8)
nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.3)
top_5_nodes = [node for node, _ in top_betweenness]
nx.draw_networkx_labels(G, pos, labels={node: node for node in top_5_nodes}, font_size=10, font_color='black', ax=ax)

sm = plt.cm.ScalarMappable(cmap=plt.cm.Greens, norm=plt.Normalize(vmin=min(node_color), vmax=max(node_color)))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label("Betweenness Centrality")

ax.axis("off")
plt.tight_layout()
plt.show()

top5_betweenness_df = pd.DataFrame(top_betweenness, columns=["Node", "Betweenness Centrality"])
fig, ax = plt.subplots(figsize=(8, 4))
norm = plt.Normalize(vmin=min(top5_betweenness_df["Betweenness Centrality"]), vmax=max(top5_betweenness_df["Betweenness Centrality"]))
colors = [plt.cm.Greens(norm(val)) for val in top5_betweenness_df["Betweenness Centrality"]]

sns.barplot(data=top5_betweenness_df, x="Betweenness Centrality", y="Node", palette=colors, ax=ax)
plt.title("Top 5 Users by Betweenness Centrality", fontsize=13)
for i, (node, centrality) in enumerate(top_betweenness):
    ax.text(centrality + 0.002, i, f"{centrality:.4f}", va='center')
sm = plt.cm.ScalarMappable(cmap=plt.cm.Greens, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label("Betweenness Centrality")
plt.tight_layout()
plt.show()

# === EIGENVECTOR CENTRALITY ===
try:
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
    top_eigenvector = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\nTop 5 by Eigenvector Centrality:")
    for node, score in top_eigenvector:
        print(f"Node {node}: {score:.4f}")
except nx.PowerIterationFailedConvergence:
    print("\nEigenvector Centrality did not converge. Try increasing max_iter.")
    eigenvector_centrality = None

if eigenvector_centrality:
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.suptitle("Facebook Ego-Network: Eigenvector Centrality Visualization", fontsize=14)

    node_color = [eigenvector_centrality[node] for node in G.nodes()]
    node_size = [5000 * eigenvector_centrality[node] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_size, node_color=node_color, cmap=plt.cm.Reds, alpha=0.8)
    nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.3)
    top_5_nodes = [node for node, _ in top_eigenvector]
    nx.draw_networkx_labels(G, pos, labels={node: node for node in top_5_nodes}, font_size=10, font_color='black', ax=ax)

    sm = plt.cm.ScalarMappable(cmap=plt.cm.Reds, norm=plt.Normalize(vmin=min(node_color), vmax=max(node_color)))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label("Eigenvector Centrality")

    ax.axis("off")
    plt.tight_layout()
    plt.show()

    top5_eigenvector_df = pd.DataFrame(top_eigenvector, columns=["Node", "Eigenvector Centrality"])
    fig, ax = plt.subplots(figsize=(8, 4))
    norm = plt.Normalize(vmin=min(top5_eigenvector_df["Eigenvector Centrality"]), vmax=max(top5_eigenvector_df["Eigenvector Centrality"]))
    colors = [plt.cm.Reds(norm(val)) for val in top5_eigenvector_df["Eigenvector Centrality"]]

    sns.barplot(data=top5_eigenvector_df, x="Eigenvector Centrality", y="Node", palette=colors, ax=ax)
    plt.title("Top 5 Users by Eigenvector Centrality", fontsize=13)
    for i, (node, centrality) in enumerate(top_eigenvector):
        ax.text(centrality + 0.002, i, f"{centrality:.4f}", va='center')
    sm = plt.cm.ScalarMappable(cmap=plt.cm.Reds, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label("Eigenvector Centrality")
    plt.tight_layout()
    plt.show()
