#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/3
# @Author  : xujun


# 用字典实现
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         word = {}
#         for i in s:
#             diff = ord(i) - ord('a')
#             if diff in word.keys():
#                 word[diff] += 1
#             else:
#                 word[diff] = 1
#         for j in t:
#             diff = ord(j) - ord('a')
#             if diff in word.keys():
#                 word[ord(j) - ord('a')] -= 1
#             else:
#                 return False
#         for value in word.values():
#             if value != 0:
#                 return False
#         return True


# 用list实现
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word = [0] * 26
        for i in s:
            word[ord(i) - ord('a')] += 1
        for j in t:
            word[ord(j) - ord('a')] -= 1
            if word[ord(i) - ord('a')] < 0:
                return False
        for value in word:
            if value != 0:
                return False
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
