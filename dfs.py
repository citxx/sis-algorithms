#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

# dfs с восстановлением пути
def dfs(graph, u, visited=None, previous=None):
    if visited is None:
        visited = [False] * len(graph)
    if previous is None:
        previous = [None] * len(graph)

    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            previous[v] = u
            dfs(graph, v, visited, previous)

    return previous

def get_path(previous, u):
    path = []
    while previous[u] is not None:
        path.append(u)
        u = previous[u]
    path.reverse()
    return path


prev = dfs(graph, 0)
print(get_path(prev, 4))
print(get_path(prev, 2))


# Проверка на наличие циклов (неориентированный случай)
def dfs(graph, u, prev=None, visited=None):
    if visited is None:
        visited = [False] * len(graph)

    visited[u] = True
    for v in graph[u]:
        if v != prev and visited[v]:
            return True
        else:
            if dfs(graph, v, u, visited):
                return True
    return False


# Проверка на наличие циклов (ориентированный случай)
WHITE, GRAY, BLACK = 0, 1, 2
def dfs(graph, u, state=None):
    if state is None:
        state = [WHITE] * len(graph)

    state[u] = GRAY

    is_cyclic = False
    for v in graph[u]:
        if state[v] == GRAY:
            is_cyclic = True
            break
        elif state[v] == WHITE:
            dfs(graph, v, state)

    state[u] = BLACK
    return is_cyclic
