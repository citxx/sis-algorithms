#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

"""Поиск в ширину на списках смежности, находящий расстояния до всех вершин."""


from collections import deque


def bfs(graph, start):
    to_visit = deque([start])
    considered = [False] * len(graph)
    considered[start] = True

    distance = [None] * len(graph)  # distance[v] - расстояние от start до v
    distance[start] = 0
    while len(to_visit) > 0:
        u = to_visit.popleft()
        for v in graph[u]:
            if not considered[v]:
                distance[v] = distance[u] + 1
                to_visit.append(v)
                considered[v] = True

    return distance


if __name__ == '__main__':
    distance = bfs([[1], [2], [1], [0]], 0)
    print(distance)
