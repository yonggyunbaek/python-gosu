# https://leetcode.com/problems/permutation-difference-between-two-strings/submissions/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        answer = 0
        t = list(t)
        for i, char in enumerate(s):
            # print(i, char)
            print(t.index(char))
            if i != t.index(char):
                answer += abs(i - t.index(char))
            
        return answer
