#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>
#   Irina Brovar <iris-arcus@yandex.ru>


# Вариант 1
def hanoi_1(source, destination, n):
    middle = 6 - (source + destination)

    if n == 1:
        print(1, source, destination)
    else:
        hanoi_1(source, middle, n - 1)
        print(n, source, destination)
        hanoi_1(middle, destination, n - 1)

hanoi_1(1, 3, 5)


# Вариант 2
def hanoi_2(n, source, middle, destination):
    if n == 1:
        print(n, source, destination)
    else:
        hanoi_2(n - 1, source, destination, middle)
        print(n, source, destination)
        hanoi_2(n - 1, middle, source, destination)

hanoi_2(3, 'A', 'B', 'C')
