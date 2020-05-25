#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14
# @Author  : xujun


"""
N叉树的前序遍历
给定一个 N 叉树，返回其节点值的前序遍历。
"""

# 递归
# class Solution:
#     def preorder(self, root):
#         res = []
#         self.helper(root, res)
#         return res
#
#     def helper(self, root, res):
#         if not root:
#             return res
#         res.append(root.val)
#         for node in root.children:
#             self.helper(node, res)


# 迭代
class Solution:
    def preorder(self, root):
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.children[::-1])
        return res
