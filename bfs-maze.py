#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Contributors:
#   Artem Tabolin <artemtab@yandex.ru>

"""Поиск в ширину на лабиринте, находящий расстояния до всех точек"""


from collections import deque

NEIGHBOURS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs(maze, start_x, start_y):
    to_visit = deque([(start_x, start_y)])
    considered = [[False] * len(row) for row in maze]
    considered[start_x][start_y] = True

    distance = [[None] * len(row) for row in maze]
    distance[start_x][start_y] = 0
    while len(to_visit) > 0:
        x, y = to_visit.popleft()
        for dx, dy in NEIGHBOURS:
            nx, ny = x + dx, y + dy
            if not considered[nx][ny] and maze[nx][ny] != '#':
                distance[nx][ny] = distance[x][y] + 1
                to_visit.append((nx, ny))
                considered[nx][ny] = True

    return distance


if __name__ == '__main__':
    distance = bfs([
        '#######',
        '#.#...#',
        '#...#.#',
        '#######'
    ], 1, 1)
    print(*distance, sep='\n')
