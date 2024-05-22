import uuid
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappush, heappop

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color="white")
    plt.show()

def depth_first_traversal(node, visit_func, colors=None):
    if node is None:
        return
    if colors is None:
        colors = {}
    visit_func(node, colors)
    depth_first_traversal(node.left, visit_func, colors)
    depth_first_traversal(node.right, visit_func, colors)

def breadth_first_traversal(node, visit_func, colors=None):
    if node is None:
        return
    if colors is None:
        colors = {}
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        visit_func(current_node, colors)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

def visualize_dfs(node):
    visited_colors = {}
    def visit(node, colors):
        if node.id not in visited_colors:
            visited_colors[node.id] = generate_color(len(visited_colors))
            node.color = visited_colors[node.id]
    depth_first_traversal(node, visit, visited_colors)
    draw_tree(node)

def visualize_bfs(node):
    visited_colors = {}
    def visit(node, colors):
        if node.id not in visited_colors:
            visited_colors[node.id] = generate_color(len(visited_colors))
            node.color = visited_colors[node.id]
    breadth_first_traversal(node, visit, visited_colors)
    draw_tree(node)

def generate_color(index):
    # Генеруємо колір залежно від індексу
    red = hex((index * 10) % 256)[2:].zfill(2)
    green = hex((index * 20) % 256)[2:].zfill(2)
    blue = hex((index * 30) % 256)[2:].zfill(2)
    return f'#{red}{green}{blue}'

# Оновлений код для побудови бінарної купи
def build_heap(elements):
    if not elements:
        return None

    nodes = [Node(val) for val in elements]
    n = len(nodes)
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]

    return nodes[0]

elements = [3, 1, 6, 5, 2, 8, 7]
heap_root = build_heap(elements)

# Візуалізація обходу в глибину
visualize_dfs(heap_root)

# Візуалізація обходу в ширину
visualize_bfs(heap_root)
