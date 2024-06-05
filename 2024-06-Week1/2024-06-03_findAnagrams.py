"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
# Counter 함수 사용
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # for loop search anagrams
        
        
        ans = []
        p_counter = Counter(p)
        # print(p_counter)
        for i in range(len(s)-len(p)+1):
            # substring words
            # print(s[i:i+len(p)])
            tmp_counter = Counter(s[i:i+len(p)])
            if tmp_counter == p_counter:
                ans.append(i)
        
        return ans

# Hash맵 사용
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []

        if len(s) < len(p):
            return ans

        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])  # 초기 윈도우
        # print(s_counter,"**")
        if p_counter == s_counter:
            ans.append(0)
        
        # 초기값 제외 문자열 부터 검색
        for i in range(len(p), len(s)):
            # 새로운 문자 추가
            s_counter[s[i]] += 1  
            
            # 윈도우의 첫 번째 문자 제거
            s_counter[s[i-len(p)]] -= 1
            if s_counter[s[i-len(p)]] == 0:
                del s_counter[s[i-len(p)]]
            
#             print(s_counter)
            # 윈도우와 p의 Counter 비교
            if s_counter == p_counter:
                ans.append(i-len(p)+1)

        return ans
