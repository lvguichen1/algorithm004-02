#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14
# @Author  : xujun

"""
N叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
"""


# 简化的广度优先搜索
# class Solution:
#     def levelOrder(self, root):
#         res = []
#         if not root:
#             return res
#         cur_level = [root]
#         while cur_level:
#             next_level = []
#             cur_res = []
#             for node in cur_level:
#                 if node:
#                     cur_res.append(node.val)
#                     next_level.extend(node.children)
#             cur_level = next_level
#             res.append(cur_res)
#         return res


# 基于队列的广度优先搜索
# class Solution:
#     def levelOrder(self, root):
#         res = []
#         if not root:
#             return res
#         import collections
#         queue = collections.deque([root])
#         while queue:
#             cur_res = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if node:
#                     cur_res.append(node.val)
#                     queue.extend(node.children)
#             res.append(cur_res)
#         return res


# 递归
class Solution:
    def levelOrder(self, root):

        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if root is not None:
            traverse_node(root, 0)
        return result
