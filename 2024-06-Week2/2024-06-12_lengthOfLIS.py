"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""
## DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        dp = [1 for _ in range(len(nums))]
        # print(dp)
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        # print(dp)
        return max(dp)

## 바이너리 서치
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                left, right = 0, len(ans) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if ans[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid - 1
                ans[left] = nums[i]
        
        return len(ans)