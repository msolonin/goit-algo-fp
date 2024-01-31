# -*- coding: utf-8 -*-
"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

    написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
    розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
    написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""
import copy


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def reverse_linked_list(llist):
    llist = copy.copy(llist)
    prev = None
    current = llist.head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return LinkedList(prev)


def merge_sorted_lists(list1, list2):
    list1 = copy.copy(list1)
    list1 = list1.head
    list2 = copy.copy(list2)
    list2 = list2.head
    initial_node = Node()
    current = initial_node
    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1 is not None:
        current.next = list1
    else:
        current.next = list2
    return LinkedList(initial_node.next)


def insertion_sort_linked_list(llist):
    llist = copy.copy(llist)
    head = llist.head
    if head is None or head.next is None:
        return llist
    sorted_head = None
    current = head
    while current is not None:
        next_node = current.next
        if sorted_head is None or sorted_head.data >= current.data:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head
            while temp.next is not None and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        current = next_node
    return LinkedList(sorted_head)


def main():
    llist = LinkedList()
    llist_2 = LinkedList()
    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print("Оригінальний список:")
    llist.print_list()
    reversed_list = reverse_linked_list(llist)
    print("Реверсований список:")
    reversed_list.print_list()

    sorted_linked_list = insertion_sort_linked_list(reversed_list)
    print("Відсортований вставками список:")
    sorted_linked_list.print_list()
    llist_2.insert_at_end(1)
    llist_2.insert_at_end(3)
    llist_2.insert_at_end(10)
    llist_2.insert_at_end(20)
    llist_2.insert_at_end(40)
    merged_list = merge_sorted_lists(sorted_linked_list, llist_2)
    print("об'єднаний список:")
    merged_list.print_list()


if __name__ == "__main__":
    main()
