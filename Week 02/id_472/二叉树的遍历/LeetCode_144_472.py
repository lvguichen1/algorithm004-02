#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14
# @Author  : xujun
"""
二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。
"""


# 递归
# class Solution:
#     def preorderTraversal(self, root):
#         # if not root 这一步在preOrder里面做了
#         res = []
#         self.preOrder(root, res)
#         return res
#
#     def preOrder(self, root, res):
#         '''对root的判空其实是在这里做了，所以原方法就不需要对root再一次判空'''
#         if not root:
#             return res
#         res.append(root.val)
#         self.preOrder(root.left, res)
#         self.preOrder(root.right, res)
#         return res

# 基于栈的遍历
class Solution:
    def preorderTraversal(self, root):
        res = []  # 结果列表
        stack = []  # 辅助栈
        cur = root  # 当前节点
        while stack or cur:
            while cur:  # 遍历到最后一层
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            top = stack.pop()  # 此时该节点的左子树已经全部遍历完
            cur = top.right  # 对右子树遍历
        return res


# 迭代
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output
