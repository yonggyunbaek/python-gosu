"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 예외 처리
        if len(nums) == 0:
            return 0
        
        
        # 1. 중복제거
        nums = sorted(list(set(nums)))
        # print(nums)
        
        dp = [0] * len(nums)
        dp[0] = 1
        # print(dp)
        
        for n in range(1,len(nums)):
            if nums[n] == nums[n-1] + 1:
                dp[n] = dp[n-1] + 1
            else:
                dp[n] = 1
                
        return max(dp)