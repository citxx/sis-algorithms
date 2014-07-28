#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>


def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1

    if n != 1 or len(factors) == 0:
        factors.append(n)

    return factors


for x in range(1, 41):
    print(x, "=", " * ".join([str(x) for x in factorize(x)]))
