#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

"""Бинпоиск корня монотонной функции."""


# Увеличивает точность в 2 ** k раз.
def find_root(left, right, f, k=20):
    # Инвариант: f(left) < 0 <= f(right)
    for i in range(k):
        middle = (left + right) / 2
        if f(middle) < 0:
            left = middle
        else:
            right = middle
    return left  # Можно вернуть что угодно


# Получает корень с точностью eps. Может зациклиться, если расстояние между
# соседними вещественными числами будет больше eps.
def dumb_find_root(left, right, f, eps):
    while right - left > eps:
        middle = (left + right) / 2
        if f(middle) < 0:
            left = middle
        else:
            right = middle
    return left  # Можно вернуть что угодно


if __name__ == '__main__':
    print(find_root(0, 1, lambda x: x ** 2 - 0.5))

    # А вот это уже зациклится
    # print(dumb_find_root(10 ** 20, 10 ** 25, lambda x: x - 10 ** 23, 1))
