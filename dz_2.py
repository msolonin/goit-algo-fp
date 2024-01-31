# -*- coding: utf-8 -*-
"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle

TREE_COLOR = "green"
BG_COLOUR = "white"


def draw_pythagoras_tree(branch_len, _turtle, recursion_level):
    if recursion_level == 0:
        return
    else:
        _turtle.forward(branch_len)
        _turtle.left(45)
        draw_pythagoras_tree(0.7 * branch_len, _turtle, recursion_level - 1)
        _turtle.right(90)
        draw_pythagoras_tree(0.7 * branch_len, _turtle, recursion_level - 1)
        _turtle.left(45)
        _turtle.backward(branch_len)


def main():
    screen = turtle.Screen()
    screen.bgcolor(BG_COLOUR)
    _turtle = turtle.Turtle()
    _turtle.color(TREE_COLOR)
    _turtle.pensize(2)
    _turtle.left(90)
    _turtle.up()
    _turtle.backward(200)
    _turtle.down()
    level = int(input("Input level of recursion: "))
    draw_pythagoras_tree(100, _turtle, level)
    # Програма закриеться після кліку на екран
    screen.exitonclick()


if __name__ == "__main__":
    main()
