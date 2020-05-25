#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7
# @Author  : xujun
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X

解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 
最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""


# DFS
# class Solution:
#     def solve(self, board) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board or not board[0]:
#             return
#         row = len(board)
#         col = len(board[0])
#
#         def dfs(i, j):
#             board[i][j] = "B"
#             for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 tmp_i = i + x
#                 tmp_j = j + y
#                 if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
#                     dfs(tmp_i, tmp_j)
#
#         for j in range(col):
#             # 第一行
#             if board[0][j] == "O":
#                 dfs(0, j)
#             # 最后一行
#             if board[row - 1][j] == "O":
#                 dfs(row - 1, j)
#
#         for i in range(row):
#             # 第一列
#             if board[i][0] == "O":
#                 dfs(i, 0)
#             # 最后一列
#             if board[i][col - 1] == "O":
#                 dfs(i, col - 1)
#
#         for i in range(row):
#             for j in range(col):
#                 # O 变成 X
#                 if board[i][j] == "O":
#                     board[i][j] = "X"
#                 # B 变成 O
#                 if board[i][j] == "B":
#                     board[i][j] = "O"


# BFS
# class Solution:
#     def solve(self, board) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board or not board[0]:
#             return
#         row = len(board)
#         col = len(board[0])
#
#         def bfs(i, j):
#             from collections import deque
#             queue = deque()
#             queue.appendleft((i, j))
#             while queue:
#                 i, j = queue.pop()
#                 if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
#                     board[i][j] = "B"
#                     for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                         queue.appendleft((i + x, j + y))
#
#         for j in range(col):
#             # 第一行
#             if board[0][j] == "O":
#                 bfs(0, j)
#             # 最后一行
#             if board[row - 1][j] == "O":
#                 bfs(row - 1, j)
#
#         for i in range(row):
#
#             if board[i][0] == "O":
#                 bfs(i, 0)
#             if board[i][col - 1] == "O":
#                 bfs(i, col - 1)
#
#         for i in range(row):
#             for j in range(col):
#                 if board[i][j] == "O":
#                     board[i][j] = "X"
#                 if board[i][j] == "B":
#                     board[i][j] = "O"


# 并查集
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
s = Solution()
s.solve(board)
