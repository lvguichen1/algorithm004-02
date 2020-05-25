#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/31
# @Author  : xujun

class Solution:
    def twoSum(self, nums, target: int):
        res = {}
        for i in range(len(nums)):
            if nums[i] in res.keys():
                return [res[nums[i]], i]
            diff = target - nums[i]
            res[diff] = i
