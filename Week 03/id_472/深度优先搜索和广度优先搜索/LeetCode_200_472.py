#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23
# @Author  : xujun
"""
岛屿数量
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
"""


class Solution:
    def numIslands(self, grid):
        def dfs(r, c):
            if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        nr = len(grid)
        nc = len(grid[0])
        if grid is None or nr == 0:
            return 0
        num_islands = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands
