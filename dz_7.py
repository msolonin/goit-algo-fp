# -*- coding: utf-8 -*-
"""
Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел,
які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел,
які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції.
Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми,
виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

Сума	Імовірність
2	2.78% (1/36)
3	5.56% (2/36)
4	8.33% (3/36)
5	11.11% (4/36)
6	13.89% (5/36)
7	16.67% (6/36)
8	13.89% (5/36)
9	11.11% (4/36)
10	8.33% (3/36)
11	5.56% (2/36)
12	2.78% (1/36)

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.
"""

import random


def simulate_dice_rolls(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        total = roll_1 + roll_2
        results.append(total)
    return results


def calculate_probabilities(results):
    final_results = dict()
    total_rolls = len(results)
    for i in range(2, 13):
        final_results[i] = results.count(i) / total_rolls
    return final_results


def emulate_dice_rolls():
    num_rolls = 100000
    dice_results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(dice_results)
    print("Сума \t Імовірність")
    for i in range(2, 13):
        print(f"{i} \t {probabilities[i] * 100:.4f} %")


if __name__ == "__main__":
    emulate_dice_rolls()
    print("\nТа еталонна таблиця ймовірностей сум при киданні двох кубиків:")
    print("""Сума	Імовірність
2	2.78% (1/36)
3	5.56% (2/36)
4	8.33% (3/36)
5	11.11% (4/36)
6	13.89% (5/36)
6	13.89% (5/36)
7	16.67% (6/36)
8	13.89% (5/36)
9	11.11% (4/36)
10	8.33% (3/36)
11	5.56% (2/36)
12	2.78% (1/36)
    """)
    print("\nЯк бачимо з наведених таблиць, імовірність кожної суми відмінна від аналітичних розрахунків несуттево")