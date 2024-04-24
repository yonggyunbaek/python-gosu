"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        check_dict = {}

        def dfs(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            # 이미 계산된 경우 재사용
            if (i, j) in check_dict:
                return check_dict[(i, j)]

            # s1과 s3가 일치하고, 해당 문자를 사용하여 재귀 호출이 성공하는 경우
            if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j, k + 1):
                check_dict[(i, j)] = True
                return True

            # s2와 s3가 일치하고, 해당 문자를 사용하여 재귀 호출이 성공하는 경우
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1, k + 1):
                check_dict[(i, j)] = True
                return True

            check_dict[(i, j)] = False
            return False

        if len(s1) + len(s2) != len(s3):
            return False

        return dfs(0, 0, 0)


## 번외 풀이 Dynamic Programming
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        if m < n:
            return self.isInterleave(s2, s1, s3)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[n]