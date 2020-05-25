#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/3
# @Author  : xujun
class Solution:
    def groupAnagrams(self, strs):
        words = {}
        for word in strs:
            letter_list = [0] * 26
            for s in word:
                letter_list[ord(s) - ord('a')] += 1
            letters = '#'.join(map(str, letter_list))
            if letters in words.keys():
                words[letters].append(word)
            else:
                words[letters] = [word]
        return list(words.values())


s = Solution()
ss = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(ss))