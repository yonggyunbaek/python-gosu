"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
"""

# 동적프로그래밍
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s)+1) # 빈문자(공백) 포함 s 문자열 길이 만큼 dp리스트
        dp[0] = True # 빈문자열의 경우를 위한 초기화
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True # p[j] : 단어의 시작지점 초기화
                    break
            
        # print(dp[len(s)])
        
        return dp[len(s)]
    
    
    
    
    
    
## 백트랙킹(재귀) // 시간초과
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        def backtrack(start):
            # 문자열의 끝에 도달한 경우
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                # 현재 부분 문자열이 wordDict에 있다면, 재귀적으로 나머지 부분 문자열을 확인
                if s[start:end] in wordSet and backtrack(end):
                    return True
            return False

        return backtrack(0)