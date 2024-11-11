# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/submissions/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        answer = 0
        
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] < target:
                    answer += 1
        
        return answer
