import uuid

import networkx as nx
import matplotlib.pyplot as plt
from heapq import *

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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_tree(root, i, heap):
    left_pos = left(i)
    right_pos = right(i)
    if left_pos < len(heap):
        root.left = Node(heap[left_pos])
        build_tree(root.left, left_pos, heap)
    if right_pos < len(heap):
        root.right = Node(heap[right_pos])
        build_tree(root.right, right_pos, heap)

def parent(i):
    return (i-1)/2
  
def left(i):
    return (2*i + 1) 

def right(i):
    return (2*i + 2)

# Створення купи у вигляді дерева
heap = [18, 15, 3, 29, 4, 7, 1, 5, 12, 9, 2, 6, 0, 8]
heapify(heap)
print(heap)
root = Node(heap[0])
build_tree(root, 0, heap)

# Відображення купи
draw_tree(root)