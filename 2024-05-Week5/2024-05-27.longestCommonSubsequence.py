"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without 
changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        # 이전 행과 현재 행을 저장할 1차원 DP 테이블을 준비합니다.
        dp_prev = [0] * (len(text2) + 1)
        
        for i in range(1, len(text1) + 1):
            dp_current = [0] * (len(text2) + 1)
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp_current[j] = 1 + dp_prev[j-1]
                else:
                    dp_current[j] = max(dp_prev[j], dp_current[j-1])
            dp_prev = dp_current
        
        # 최대값 반환
        return dp_prev[-1]
    
    

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp 테이블 초기화
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # dp 테이블 채우기
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # 가장 긴 공통 부분 수열의 길이 반환
        return dp[len(text1)][len(text2)]
