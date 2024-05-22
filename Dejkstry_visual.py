import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

def dijkstra(graph, start_vertex):
    V = graph.V
    distances = [float('inf')] * V
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    path = [-1] * V
    visited = [False] * V

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if visited[current_vertex]:
            continue
        visited[current_vertex] = True

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, path

def draw_graph(graph, pos, ax):
    G = nx.Graph()
    for u in range(graph.V):
        for v, w in graph.graph[u]:
            G.add_edge(u, v, weight=w)

    edge_labels = {(u, v): w for u, v, w in G.edges(data='weight')}
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

def animate_dijkstra(graph, start_vertex):
    V = graph.V
    distances = [float('inf')] * V
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    G = nx.Graph()
    for u in range(graph.V):
        for v, w in graph.graph[u]:
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)

    fig, ax = plt.subplots()
    draw_graph(graph, pos, ax)
    plt.show(block=False)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

                draw_graph(graph, pos, ax)
                nx.draw_networkx_nodes(G, pos, nodelist=[neighbor], node_color='red', node_size=700, ax=ax)
                plt.pause(0.5)

    plt.show()

# Створення графа
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

# Анімація алгоритму Дейкстри
animate_dijkstra(g, 0)
