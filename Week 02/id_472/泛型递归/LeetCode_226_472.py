#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26
# @Author  : xujun
"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# class Solution:
#     def invertTree(self, root):
#         if not root:
#             return root
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             node.left, node.right = node.right, node.left
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return root


class Solution:
    def invertTree(self, root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
