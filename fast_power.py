#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Irina Brovar <iris-arcus@yandex.ru>

# Быстрое возведение в степень
def fast_power(number, power):
    if power == 0:
        return 1
    if power % 2 == 0:
        return fast_power(number * number, power // 2)
    else:
        return fast_power(number, power - 1) * number

# Быстрое возведение в степень без рекурсии в цикле
def fast_power_loop(number, power):
    answer = 1
    while power > 0:
        if power % 2 == 0:
            number *= number
            power //= 2
        else:
            answer *= number
            power -= 1
    return answer


print(fast_power(2, 32), fast_power_loop(2, 32), 2 ** 32)
print(fast_power(5, 3), fast_power_loop(5, 3), 5 ** 3)
print(fast_power(5, 1), fast_power_loop(5, 1), 5 ** 1)
print(fast_power(4, 4), fast_power_loop(4, 4), 4 ** 4)
