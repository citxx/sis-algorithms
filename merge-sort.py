#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

# Выделяем дополнительный массив. Merge одним for'ом с хитрым условием.
def merge_sort(a, left=0, right=None, storage=None):
    if right is None:
        right = len(a)
    if storage is None:
        storage = a[:]

    if right - left > 1:
        middle = (left + right) // 2
        merge_sort(a, left, middle, storage)
        merge_sort(a, middle, right, storage)
        merge(a, left, middle, right, storage)


def merge(a, left, middle, right, storage):
    i, j = left, middle
    for k in range(left, right):
        if i < middle and (j == right or a[i] <= a[j]):
            storage[k] = a[i]
            i += 1
        else:
            storage[k] = a[j]
            j += 1

    for k in range(left, right):
        a[k] = storage[k]
