# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/submissions/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        tmp = []
        for num in nums:
            if num in tmp:
                answer.append(num)
            else:
                tmp.append(num)
        return answer
            
