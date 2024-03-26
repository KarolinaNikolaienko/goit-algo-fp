# Завдання 3. Дерева, алгоритм Дейкстри

# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших 
# шляхів від початкової вершини до всіх інших.

import networkx as nx
import matplotlib.pyplot as plt
import math
import heapq

def dijkstra(graph, start):
    distances = {}
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)
        if node in distances:
            continue 
        distances[node] = dist
        for neighbor, weight in graph[node].items():
            if neighbor not in distances:
                heapq.heappush(heap, (dist + weight["weight"], neighbor))

    return distances

def main():
    graph = {
        "New York" : ["London", "Rio de Janeiro", "Aleksandria", "Cape Town"],
        "London" : ["New York", "Rio de Janeiro"],
        "Aleksandria" : ["Dubai", "London", "New York", "Rio de Janeiro"],
        "Sydney" : ["Cape Town", "Mumbai", "Singapore", "Tokio"],
        "Dubai": ["Mumbai", "Singapore", "Aleksandria", "Sydney", "Cape Town"],
        "Tokio" : ["Singapore"],
        "Cape Town" : ["New York", "Rio de Janeiro", "London", "Sydney"],
        "Rio de Janeiro" : ["New York", "Cape Town", "London"],
        "Mumbai" : ["Dubai", "Sydney", "Singapore"],
        "Singapore" : ["Tokio", "Cape Town", "Mumbai", "Dubai"]
    }

    G = nx.Graph(graph)
    pos = {}
    coord = [(10, 100), (30, 105), (50, 90), (110, 10), (60, 80), (110, 100), (40, 15), 
             (20, 18), (80, 70), (100, 50)]
    for i, node in enumerate(G.nodes()):
        pos[node] = coord[i]
    #nx.draw(G, pos, with_labels=True, arrows=True)
    
    # Додаємо вагу для ребер - відстань між точками
    for edge in G.edges():
        G[edge[0]][edge[1]]["weight"] = math.dist(pos[edge[0]],pos[edge[1]])
    
    print(dijkstra(G, "New York"))

    #plt.show()

if __name__ == "__main__":
    main()