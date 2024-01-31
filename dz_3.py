# -*- coding: utf-8 -*-
"""
Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу.
Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших
шляхів від початкової вершини до всіх інших.
"""
import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances


def main():
    # Розрахунок найкоротших шляхів
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 3}
    }

    start_vertex = 'A'
    result = dijkstra(graph, start_vertex)
    print(f"Найкоротші шляхи від вершини {start_vertex}: {result}")
    # Візуалізація графа
    G = nx.Graph()
    for k, v in graph.items():
        G.add_node(k)
        for neighbor, weight in v.items():
            G.add_edge(k, neighbor, weight=weight)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=3)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


if __name__ == "__main__":
    main()
