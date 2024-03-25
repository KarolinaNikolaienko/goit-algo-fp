import uuid

import networkx as nx
import matplotlib.pyplot as plt
from colour import Color

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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

def draw_tree(tree_root, title = ""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    

i = 0
def dfs(root):
    if not root:
        return
    global i
    root.color = colors_green[i].get_hex()
    i += 1
    if root.left:
        dfs(root.left)
    if root.right:
        dfs(root.right)

j = 0
def bfs(root):
    if not root:
        return
    global j
    if root.left:
        root.left.color = colors_purple[j].get_hex()
        j += 1
    if root.right:
        root.right.color = colors_purple[j].get_hex()
        j += 1
    if root.left:
        bfs(root.left)
    if root.right:
        bfs(root.right)
    

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

colors_purple = list(Color("#5B2C6F").range_to(Color("#F4ECF7"),15))
colors_green = list(Color("#186A3B").range_to(Color("#EAFAF1"),15))

dfs(root)
# Відображення дерева
draw_tree(root, "DFS")

root.color = colors_purple[j].get_hex()
j += 1
bfs(root)
# Відображення дерева
draw_tree(root, "BFS")

plt.show()
