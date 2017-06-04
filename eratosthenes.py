#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>


def sieve(n):
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


n = 30
is_prime = sieve(n)
for i in range(2, n + 1):
    if is_prime[i]:
        print(i)
