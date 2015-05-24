#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

from bisect import bisect_right


# Сортировка выбором минимума. O(n^2) сравнений. O(n) перемещений.
# O(1) дополнительной памяти. Нестабильная.
def choice_sort(a):
    for i in range(len(a)):
        min_index = i + a[i:].index(min(a[i:]))
        a[min_index], a[i] = a[i], a[min_index]


# Сортировка вставками. O(n * log(n)) сравнений. O(n^2) перемещений.
# O(1) дополнительной памяти. Cтабильная.
def insertion_sort(a):
    for i in range(1, len(a)):  # На i-ой итерации список a[:i] отсортирован.
        insert_pos = bisect_right(a, a[i], 0, i)
        a[insert_pos:i + 1] = [a[i]] + a[insert_pos:i]


if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    b = a[:]

    choice_sort(a)
    print("Choice: ", a)
    insertion_sort(b)
    print("Insert: ", b)
