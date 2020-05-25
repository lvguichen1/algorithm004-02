#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14
# @Author  : xujun


"""
N叉树的后序遍历
给定一个 N 叉树，返回其节点值的后序遍历。
"""


# 递归
# class Solution:
#     def postorder(self, root):
#         res = []
#         self.helper(root, res)
#         return res
#
#     def helper(self, root, res):
#         if root:
#             res.append(root.val)
#             for node in root.children[::-1]:
#                 self.helper(node, res)

# 迭代
class Solution:
    def postorder(self, root):
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if not root:
                return res
            stack.extend(root.children)
            res.append(root.val)
        return res[::-1]
