#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26
# @Author  : xujun
"""
二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# 广度优先遍历
# class Solution:
#     def maxDepth(self, root) -> int:
#         depth = 0
#         if not root:
#             return depth
#         cur_layer = [root]
#         while cur_layer:
#             next_layer = []
#             depth += 1
#             for node in cur_layer:
#                 if node.left:
#                     next_layer.append(node.left)
#                 if node.right:
#                     next_layer.append(node.right)
#             cur_layer = next_layer
#         return depth


# 深度优先遍历-递归
# class Solution:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         else:
#             left_height = self.maxDepth(root.left)
#             right_height = self.maxDepth(root.right)
#             return max(left_height, right_height) + 1

# 深度优先遍历-迭代
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth
