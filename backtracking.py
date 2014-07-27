#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>


def get_all_subsets(superset, i=0, chosen=None):
    if chosen is None:
        chosen = []

    if i == len(superset):
        print(chosen)
    else:
        get_all_subsets(superset, i + 1, chosen)

        chosen.append(superset[i])
        get_all_subsets(superset, i + 1, chosen)
        chosen.pop()


def get_subsets_of_size(superset, k, i=0, chosen=None):
    if chosen is None:
        chosen = []

    if len(chosen) == k:
        print(chosen)
    else:
        # Если осталось элементов строго больше, чем нам ещё нужно набрать,
        # то можно не взять очередной элемент
        if len(superset) - i > k - len(chosen):
            get_subsets_of_size(superset, k, i + 1, chosen)

        chosen.append(superset[i])
        get_subsets_of_size(superset, k, i + 1, chosen)
        chosen.pop()


get_all_subsets([1, 2, 3, 4, 5])
get_subsets_of_size([1, 2, 3, 4, 5], 3)
