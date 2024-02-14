"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans_set = set()
        for s_char in s:
            if s_char not in ans_set:
                ans_set.add(s_char)
            else:
                ans_set.remove(s_char)
                
        return len(s) - len(ans_set) + 1 if len(ans_set) >= 1 else len(s)
    
"""
set의 활용

1. element 추가 add()
2. element 제거 remove()
3. element 모두제거 clear()
"""