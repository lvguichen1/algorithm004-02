#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21
# @Author  : xujun
"""
二进制矩阵中的最短路径

在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

"""

# BFS
# class Solution:
#     def shortestPathBinaryMatrix(self, grid) -> int:
#         from collections import deque
#
#         N = len(grid)
#
#         def is_clear(cell):
#             return grid[cell[0]][cell[1]] == 0
#
#         def get_neighbours(cell):
#             (i, j) = cell
#             return (
#                 (i + a, j + b)
#                 for a in (-1, 0, 1)
#                 for b in (-1, 0, 1)
#                 if a != 0 or b != 0
#                 if 0 <= i + a < N
#                 if 0 <= j + b < N
#                 if is_clear((i + a, j + b))
#             )
#
#         start = (0, 0)
#         goal = (N - 1, N - 1)
#
#         queue = deque()
#         if is_clear(start):
#             queue.append(start)
#         visited = set()
#         path_len = {start: 1}
#
#         while queue:
#             cell = queue.popleft()
#             if cell in visited:
#                 continue
#             if cell == goal:
#                 return path_len[cell]
#             visited.add(cell)
#             for neighbour in get_neighbours(cell):
#                 if neighbour not in path_len:
#                     path_len[neighbour] = path_len[cell] + 1
#                 queue.append(neighbour)
#
#         return -1


# A* 搜索
import heapq


class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        elif n <= 2:
            return n

        def heuristic(x, y):
            return max(abs(n - 1 - x), abs(n - 1 - y))

        h = []
        # 数据结构堆（heap）是一种优先队列。使用优先队列能够以任意顺序增加对象，并且能在任意的时间（可能在增加对象的同时）找到（也可能移除）最小的元素23
        heapq.heappush(h, (0, (0, 0, 1)))
        visited = set()
        while h:
            _, (i, j, step) = heapq.heappop(h)

            if (i, j) in visited:
                continue
            visited.add((i, j))

            for dx, dy in [(-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1)]:
                next_i, next_j = i + dx, j + dy

                if next_i == n - 1 and next_j == n - 1:
                    return step + 1

                if 0 <= next_i < n and 0 <= next_j < n and grid[next_i][next_j] == 0 and (next_i, next_j) not in visited:
                    heapq.heappush(h, (step + heuristic(next_i, next_j), (next_i, next_j, step + 1)))
        return -1


arr = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
s = Solution()
s.shortestPathBinaryMatrix(arr)
