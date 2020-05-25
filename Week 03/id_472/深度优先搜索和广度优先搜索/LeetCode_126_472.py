#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/22
# @Author  : xujun
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        length = len(beginWord)
        subwords_dict = defaultdict(list)
        for word in wordList:
            for i in range(length):
                intermediate_word = word[:i] + "*" + word[i + 1:]
                subwords_dict[intermediate_word].append(word)
        visited = set()
        total = []
        queue = [(beginWord, [])]
        while queue:
            current_word, prev = queue.pop(0)
            visited.add(current_word)
            for i in range(length):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in subwords_dict[intermediate_word]:
                    if word in visited:
                        prev.append(word)
                        if word == endWord:
                            total.append(prev)
                        else:
                            queue.append([word, prev])
            subwords_dict[intermediate_word] = []
        return total



