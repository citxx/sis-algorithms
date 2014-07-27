#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

"""Поиск в ширину на списках смежности, находящий пути до всех вершин."""


from collections import deque


def bfs(graph, start):
    to_visit = deque([start])
    considered = [False] * len(graph)
    considered[start] = True

    previous = [None] * len(graph)  # previous[v] - вершина, предшествующая
                                    # вершине v в кратчайшем пути от start.
    while len(to_visit) > 0:
        u = to_visit.popleft()
        for v in graph[u]:
            if not considered[v]:
                previous[v] = u
                to_visit.append(v)
                considered[v] = True

    return previous


def restore_path(previous, finish):
    path = []

    v = finish
    while v is not None:
        path.append(v)
        v = previous[v]

    path.reverse()
    return path


if __name__ == '__main__':
    previous = bfs([[1], [2], [1], [0]], 0)
    print(restore_path(previous, 2))
