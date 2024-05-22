import heapq
# Створення Графа
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Кількість вершин
        self.graph = [[] for _ in range(vertices)]  # Список суміжності

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))  # Додаємо ребро з вершини u до вершини v з вагою weight
        self.graph[v].append((u, weight))  # Якщо граф неорієнтований, додаємо ребро у зворотньому напрямку

# Створення купи
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, key, value):
        heapq.heappush(self.heap, (key, value))

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
    
#алгоритм Дейкстри
def dijkstra(graph, start_vertex):
    V = graph.V
    distances = [float('inf')] * V  # Ініціалізуємо всі відстані як нескінченність
    distances[start_vertex] = 0     # Відстань від початкової вершини до самої себе дорівнює 0
    min_heap = MinHeap()
    min_heap.push(0, start_vertex)

    while not min_heap.is_empty():
        current_distance, current_vertex = min_heap.pop()

        # Якщо знайдена відстань більша за вже знайдену, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстані до сусідів поточної вершини
        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдена нова коротша відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                min_heap.push(distance, neighbor)

    return distances

# Приклад використання
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

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів від вершини 0
distances = dijkstra(g, 0)

# Виведення результату
print("Відстані від початкової вершини 0 до всіх інших вершин:")
for i in range(len(distances)):
    print(f"Вершина {i} -> Відстань {distances[i]}")
