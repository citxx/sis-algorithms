#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

# Бинпоиск для детей
# Задано некоторое условие (например, array[i] < x), которое истинно в начале списка
# и ложно в оставшейся его части. Бинпоиск находит два соседних элемента, на которых
# значение этого условия изменяется.
def binary_search(array, x):
    # Инвариант array[left] < x == True, array[right] < x == False
    # Обращений к -1 и к len(array)-ому элементам никогда не происходит
    left, right = -1, len(array)
    while left + 1 < right:  # Заканчиваем, когда left и right идут друг за
                             # другом.
        middle = (left + right) // 2  # Никогда не равен ни left, ни right.
        if array[middle] < x:  # Сохраняем инвариант
            left = middle
        else:
            right = middle
    return right  # Вернуть можно как left, так и right, в зависимости от задачи.


print(binary_search([1, 5, 6, 7, 9, 15], 6))
print(binary_search([1, 5, 6, 7, 9, 15], 0))
print(binary_search([1, 5, 6, 7, 9, 15], 20))


# Бинпоиск в реальной жизни
# Здесь f - функция, принимающая на первой половине элементов значение True,
# а на второй - False.
def binary_search(array, f):
    # Инвариант f(array[left]) == true, f(array[right]) == false
    # Обращений к -1 и к len(array)-ому элементам никогда не происходит
    left, right = -1, len(array)
    while left < right - 1:  # Заканчиваем, когда left и right идут друг за 
                             # другом.
        middle = (left + right) // 2  # Никогда не равен ни left, ни right.
        if f(array[middle]):  # Сохраняем инвариант
            left = middle
        else:
            right = middle
    return right  # Вернуть можно как left, так и right, в зависимости от задачи.


print(binary_search([1, 5, 6, 7, 9, 15], lambda x: x < 6))
print(binary_search([1, 5, 6, 7, 9, 15], lambda x: x < 0))
print(binary_search([1, 5, 6, 7, 9, 15], lambda x: x < 20))

# Правый бинпоиск элемента y в a: Найти такой i, что:
# 1) Для всех e in a[:i] e <= y
# 2) Для всех e in a[i:] y < e
# binary_search(a, lambda x: x <= y)

# Левый бинпоиск элемента y в a: Найти такой i, что:
# 1) Для всех e in a[:i] e < y
# 2) Для всех e in a[i:] y <= e
# binary_search(a, lambda x: x < y)

# Также это дело легко и интуитивно понятно адаптируется к куче других
# различных случаев.
