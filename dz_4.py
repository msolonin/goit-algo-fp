# -*- coding: utf-8 -*-
"""
Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
"""
import heapq
import copy
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


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
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def create_similar_structure(nums):
    nums = copy.copy(nums)
    heapq.heapify(nums)
    root = Node(nums[0])
    level_items = 0
    parent_items = [root]
    while True:
        new_parents_items = []
        for parent_item in parent_items:
            try:
                parent_item.left = Node(nums[2 * level_items + 1])
                parent_item.right = Node(nums[2 * level_items + 2])
            except IndexError:
                return root
            level_items += 1
            new_parents_items += [parent_item.left, parent_item.right]
        parent_items = new_parents_items


if __name__ == '__main__':
    nums = [4, 10, 3, 5, 1, 8, 6, 44, 7, 22, 11, 99, 77, 88, 33, 55]
    root = create_similar_structure(nums)
    draw_tree(root)
