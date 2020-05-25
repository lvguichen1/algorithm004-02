#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3
# @Author  : xujun
"""
从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not (preorder and inorder):
            return None
        root = TreeNode(preorder[0])
        preorder.pop(0)
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root
