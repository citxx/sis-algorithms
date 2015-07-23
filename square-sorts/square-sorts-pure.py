#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>


# Сортировка пузырьком. O(n^2) сравнений. O(n^2) перемещений.
# O(1) дополнительной памяти. Стабильная.
def bubble_sort(a):
    for k in range(1, len(a)):  # После k-ой итерации "всплывут" k максимальных
                                # элементов.
        for i in range(len(a) - k):  # Не рассматриваем последние k элементов,
                                     # так как они уже на месте
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]


# Сортировка выбором минимума. O(n^2) сравнений. O(n) перемещений.
# O(1) дополнительной памяти. Нестабильная.
def choice_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[min_index], a[i] = a[i], a[min_index]


# Сортировка вставками. O(n^2) сравнений. O(n^2) перемещений.
# O(1) дополнительной памяти. Cтабильная. Количество сравнений можно довести до
# O(n * log(n)), если использовать бинпоиск места вставки.
def insertion_sort(a):
    for i in range(1, len(a)):  # На i-ой итерации список a[:i] отсортирован.
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    b, c = a[:], a[:]

    bubble_sort(a)
    print("Bubble: ", a)
    choice_sort(b)
    print("Choice: ", b)
    insertion_sort(c)
    print("Insert: ", c)
