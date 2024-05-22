"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
"""

## 동적 프로그래밍
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 예외 처리
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        # dp 배열 초기화
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]



## 재귀, 개쓰레기 풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_money(tmp, index):
            for i in range(index+2, len(nums)):
                # print(i)
                tmp += nums[i]
                rob_money(tmp, i)
                
            return tmp
        
        if len(nums) <= 2:
            return max(nums)
        
        max_amount = 0

        for n in range(len(nums)):
            # print(f'***{n}')
            tmp = 0
            tmp_money = rob_money(tmp, n)
            
            max_amount = max(max_amount,tmp_money)
            # print(max_amount)
        return max_amount