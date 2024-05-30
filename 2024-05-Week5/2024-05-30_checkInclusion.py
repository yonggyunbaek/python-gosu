"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        permutation을 구하지 않고, element의 종류와 그 갯수가 일치하면 True
        """
        
        len_s1 = len(s1)
        len_s2 = len(s2)

        
        # s1, s2 element 조사, 초기화
        s1_count, s2_count = Counter(s1), Counter(s2[:len_s1])

        # 예외처리
        if len_s1 > len_s2:
            return False
        if s1_count == s2_count:
            return True

        # 한글자 추가, 제거 O(n)
        for i in range(len_s1, len_s2):
            old = s2[i - len_s1]
            new = s2[i]

            # 윈도우에서 벗어나는 문자의 개수를 줄임
            s2_count[old] -= 1
            if s2_count[old] == 0:
                del s2_count[old]

            s2_count[new] += 1

            # element 동일할 때
            if s1_count == s2_count:
                return True

        return False
