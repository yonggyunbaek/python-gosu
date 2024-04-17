"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)# 5, 3
        dp = [list(range(n+1))] + [[r+1] + [0]*n for r in range(m)]
        # ex) [[0, 1, 2, 3], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0], [5, 0, 0, 0]]
        
        for i in range(m):
            for j in range(n):
                # dp[i+1][j+1] = dp[i][j] if word1[i]==word2[j] else min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                
                # 위와 같은 코드
                if word1[i] == word2[j]: 
                    dp[i+1][j+1] = dp[i][j]
                else:# 
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                
        return dp[m][n]

"""
1. 교체 연산
정의: word1의 i번째 문자와 word2의 j번째 문자가 서로 다를 때, word1의 i번째 문자를 word2의 j번째 문자로 교체합니다.
연산 횟수 계산: dp[i][j] = dp[i-1][j-1] + 1
설명: word1의 첫 i-1글자와 word2의 첫 j-1글자까지 이미 최소 연산으로 일치시킨 상태에서, word1의 i번째와 word2의 j번째 문자를 교체하면 두 문자열의 첫 i글자와 첫 j글자가 일치하게 됩니다. 따라서, 이전 단계의 최소 연산 횟수에 교체 연산 1회를 추가한 값이 됩니다.

2. 삽입 연산
정의: word1에 word2의 j번째 문자를 삽입합니다.
연산 횟수 계산: dp[i][j] = dp[i][j-1] + 1
설명: word1의 첫 i글자를 이미 word2의 첫 j-1글자로 변환한 상태에서, word2의 j번째 문자를 word1에 추가하면 word1이 word2의 첫 j글자와 일치하게 됩니다. 따라서, 이전 단계의 최소 연산 횟수에 삽입 연산 1회를 추가한 값이 됩니다.

3. 삭제 연산
정의: word1의 i번째 문자를 삭제합니다.
연산 횟수 계산: dp[i][j] = dp[i-1][j] + 1
설명: word1의 첫 i-1글자를 이미 word2의 첫 j글자로 변환한 상태에서, word1의 i번째 문자를 삭제하면 word1이 word2의 첫 j글자와 일치하게 됩니다. 따라서, 이전 단계의 최소 연산 횟수에 삭제 연산 1회를 추가한 값이 됩니다.
이러한 연산들을 통해 각 단계에서 문자열을 변환하는 최소 연산 횟수를 계산할 수 있습니다. 동적 계획법을 사용함으로써, 각 단계의 최소 연산 횟수를 효율적으로 계산하고 저장함으로써, 최종적으로 두 문자열 간의 최소 변환 연산 횟수를 찾아낼 수 있습니다.
"""