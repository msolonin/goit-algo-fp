# -*- coding: utf-8 -*-
"""
Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python,
яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0).
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу.
Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
"""
from matplotlib.animation import FuncAnimation
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

DEFAULT_COLOR = "#1296F0"


class Node:
    def __init__(self, key, color=DEFAULT_COLOR):
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


def depth_first_search_order(root):
    order = []
    def dfs(node):
        if node is not None:
            order.append(node.id)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return order


def breadth_first_search_order(root):
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.id)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def lighten_color(hex_color, index):
    factor = index * 0.15
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    new_rgb_color = tuple(int(value + (255 - value) * factor) for value in rgb_color)
    new_hex_color = "#{:02x}{:02x}{:02x}".format(*new_rgb_color)
    return new_hex_color


def visualize_tree_traversal(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    visited = []
    if traversal_type == 'dfs':
        traversal_order = depth_first_search_order(tree_root)
    elif traversal_type == 'bfs':
        traversal_order = breadth_first_search_order(tree_root)

    def update(frame):
        nonlocal visited
        visited.append(traversal_order[frame])
        plt.clf()
        node_colors = [node[1]['color'] for node in tree.nodes(data=True)]
        for index, data in enumerate(tree.nodes(data=True)):
            if data[0] in visited:
                node_colors[index] = lighten_color(DEFAULT_COLOR, index)
        # node_colors[frame] = NEW_COLOUR
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)

    fig, ax = plt.subplots()
    frames = list(range(len(tree.nodes)))
    ani = FuncAnimation(fig, update, frames=frames, repeat=False)
    plt.show()


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    visualize_tree_traversal(root, 'dfs')
    visualize_tree_traversal(root, 'bfs')
