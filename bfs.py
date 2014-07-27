#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

"""Поиск в ширину на списках смежности, выделяющий компоненту связности"""


from collections import deque


def bfs(graph, start):
    to_visit = deque([start])
    considered = [False] * len(graph)  # considered[v] - добавлялась ли вершина
                                       #                 v в очередь.
    considered[start] = True

    while len(to_visit) > 0:
        u = to_visit.popleft()
        for v in graph[u]:
            if not considered[v]:
                to_visit.append(v)
                considered[v] = True

    return considered


if __name__ == '__main__':
    visited = bfs([[1], [2], [1], [0]], 0)
    print([v for v in range(len(visited)) if visited[v]])
