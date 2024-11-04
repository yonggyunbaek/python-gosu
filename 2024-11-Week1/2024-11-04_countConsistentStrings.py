# https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        answer = 0
        allowed = list(allowed)

        for word in words:
            allow = 0
            for char in word:
                if char not in allowed:
                    allow = 1
            
            if allow == 0:
                answer += 1
            else:
                continue
        
        return answer
                
