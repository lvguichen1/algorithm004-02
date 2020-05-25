#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14
# @Author  : xujun
"""
二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。
"""


# 递归
# class Solution(object):
#     def postOrderTraversal(self, root):
#         res = []
#         self.postOrder(root, res)
#         return res
#
#     def postOrder(self, root, res):
#         if not root:
#             return res
#         self.postOrder(root.left, res)
#         self.postOrder(root.right, res)
#         res.append(root.val)

# 基于栈的遍历
# class Solution:
#     def postorderTraversal(self, root):
#         res = []
#         stack = []
#         cur = root
#         while stack or cur:
#             while cur:
#                 res.append(cur.val)
#                 stack.append(cur)
#                 cur = cur.right  # 先将右节点压栈
#             top = stack.pop()  # 此时该节点的右子树已经全部遍历完
#             cur = top.left  # 对左子树遍历
#         return res[::-1]  # 结果翻转

# 迭代
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        return output[::-1]
