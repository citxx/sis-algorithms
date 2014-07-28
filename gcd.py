#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


print("gcd(24, 34) =", gcd(24, 34))
