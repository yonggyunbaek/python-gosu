# https://leetcode.com/problems/build-array-from-permutation/submissions/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            answer.append(nums[i])
        
        return answer
