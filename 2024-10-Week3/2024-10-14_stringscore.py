# https://leetcode.com/problems/score-of-a-string/submissions/

class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0 
        
        for i, char in enumerate(s):
            # print(i, char)
            if i == 0:
                tmp = ord(char)
                continue
            
            answer += abs(tmp - ord(char))
            tmp = ord(char)
        return answer
