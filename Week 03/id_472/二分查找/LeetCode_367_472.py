#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1
# @Author  : xujun
"""
有效的完全平方数
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            square = mid ** 2
            if square > num:
                right = mid - 1
            elif square < num:
                left = mid + 1
            else:
                return True
        return False
