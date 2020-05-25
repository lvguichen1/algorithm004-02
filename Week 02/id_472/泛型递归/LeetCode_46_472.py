#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11
# @Author  : xujun
from typing import List


# class Solution:
#
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def dfs(nums, size, depth, hash_set, path, res):
#             if depth == size:
#                 res.append(path[:])
#                 return
#
#             for i in range(size):
#                 if not nums[i] in hash_set:
#                     hash_set.add(nums[i])
#                     path.append(nums[i])
#
#                     dfs(nums, size, depth + 1, hash_set, path, res)
#                     path.pop()
#                     hash_set.remove(nums[i])
#
#         size = len(nums)
#         if size == 0:
#             return []
#         res = []
#         path = []
#         hash_set = set()
#         dfs(nums, size, 0, hash_set, path, res)
#         return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, state, res):
            if depth == size:
                res.append(path)
                return

            for i in range(size):
                if ((state >> i) & 1) == 0:
                    dfs(nums, size, depth + 1, path + [nums[i]], state ^ (1 << i), res)

        size = len(nums)
        if size == 0:
            return []

        state = 0
        res = []
        dfs(nums, size, 0, [], state, res)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)

