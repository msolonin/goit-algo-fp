# -*- coding: utf-8 -*-
"""
Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного
програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника,
де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій
до вартості, не перевищуючи заданий бюджет.
Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний
набір страв для максимізації калорійності при заданому бюджеті.
"""
ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

MAX_COST = 100


def greedy_algorithm(max_cost):
    """Алгоритм жадібного алгоритму"""
    items_copy = sorted(ITEMS.items(), key=lambda x: x[1]['cost'] / x[1]['calories'])
    total_cost = 0
    total_calories = 0
    result = []
    for item in items_copy:
        item_cost = item[1]['cost']
        if total_cost + item_cost <= max_cost:
            result.append(item[0])
            total_cost += item_cost
            total_calories += item[1]['calories']
    return {'items': result, 'calories': total_calories, 'cost': total_cost}


def dynamic_programming(max_cost):
    """Алгоритм динамічного програмування"""
    items_copy = sorted(ITEMS.items(), key=lambda x: x[1]['cost'] / x[1]['calories'])
    n = len(items_copy)
    dp = [[0 for _ in range(max_cost + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        item = items_copy[i - 1]
        item_cost = item[1]['cost']
        item_calories = item[1]['calories']
        for j in range(1, max_cost + 1):
            if item_cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_cost] + item_calories)
            else:
                dp[i][j] = dp[i - 1][j]
    result = []
    j = max_cost
    for i in range(n, 0, -1):
        if dp[i][j] > dp[i - 1][j]:
            result.append(items_copy[i - 1][0])
            j -= items_copy[i - 1][1]['cost']
    return {'items': result, 'calories': dp[n][max_cost], 'cost': max_cost}


if __name__ == '__main__':
    print(greedy_algorithm(MAX_COST))
    print(dynamic_programming(MAX_COST))
