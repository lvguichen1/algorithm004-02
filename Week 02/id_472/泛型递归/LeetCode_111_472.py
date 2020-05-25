#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26
# @Author  : xujun
"""
二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


# 迭代
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [(root, 1)]
        min_depth = float('inf')
        while stack:
            root, depth = stack.pop()
            if not root:
                continue
            if root.left is None and root.right is None:
                if depth < min_depth:
                    min_depth = depth
            stack.append((root.left, depth + 1))
            stack.append((root.right, depth + 1))
        return min_depth
