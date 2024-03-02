import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створення графа, який може представляти соціальну мережу
G = nx.Graph()

# Додавання вершин та ребер з вагами
G.add_edge("Anna", "Max", weight=2)
G.add_edge("Anna", "Dima", weight=5)
G.add_edge("Max", "Liana", weight=1)
G.add_edge("Dima", "Orest", weight=3)
G.add_edge("Liana", "Orest", weight=4)
G.add_edge("Liana", "Anna", weight=2)
G.add_edge("Orest", "George", weight=6)
G.add_edge("Dima", "George", weight=2)

# Візуалізація графа
plt.figure(figsize=(10, 7))
nx.draw(
    G,
    with_labels=True,
    node_color="skyblue",
    node_size=700,
    edge_color="k",
    linewidths=1,
    font_size=15,
    font_weight="bold",
)
plt.title("Social Network Graph")
plt.show()

# Аналіз основних характеристик графа
number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
average_degree = sum(dict(G.degree()).values()) / number_of_nodes

print(f"Number of nodes: {number_of_nodes}")
print(f"Number of edges: {number_of_edges}")
print(f"Average degree: {average_degree:.2f}")


def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in set(graph.neighbors(start)) - visited:
        DFS(graph, next_node, visited)
    return visited


# Використання DFS з "Anna" як початковою точкою
print("DFS обхід від Anna:")
visited_nodes_dfs = DFS(G, "Anna")
print("Відвідані вершини DFS:", visited_nodes_dfs)


# Функція BFS
def BFS(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)
    return visited


# Використання BFS з "Anna" як початковою точкою
print("\nBFS обхід від Anna:")
visited_nodes_bfs = BFS(G, "Anna")
print("Відвідані вершини BFS:", visited_nodes_bfs)

path_length, path_nodes = nx.single_source_dijkstra(G, source="Anna", target="George")

print(f"Найкоротший шлях від Anna до George: {path_nodes}")
print(f"Довжина шляху: {path_length}")
