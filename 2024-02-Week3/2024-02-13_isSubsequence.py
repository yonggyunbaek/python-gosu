"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
#풀이1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        for t_char in t:
            if s_idx == len(s):
                break
            if t_char == s[s_idx]:
                s_idx += 1
        return s_idx == len(s)

# 풀이2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)