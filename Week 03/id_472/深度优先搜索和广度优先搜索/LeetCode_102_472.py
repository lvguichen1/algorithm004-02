#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18
# @Author  : xujun
"""
二叉树的层次遍历
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""


# 递归
class Solution:
    def levelOrder(self, root):
        def helper(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        res = []
        helper(root, 0)
        return res


# 迭代
from collections import deque


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return levels
