#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19
# @Author  : xujun
from collections import deque


class Solution:
    def largestValues(self, root):
        if not root:
            return []

        result = []

        q = [(root, 0)]

        while q:
            curr, level = q.pop(0)

            if level == len(result):
                result.append(curr.val)
            result[level] = max(result[level], curr.val)

            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))

        return result



