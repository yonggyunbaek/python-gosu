"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

## 해쉬맵 풀이 
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_dict = defaultdict(int)
        nums_dict[0] = 1
        
        # print(nums_dict)
        ans = 0
        tmp_sum = 0
        for n in nums:
            tmp_sum += n
            if tmp_sum - k in nums_dict:
                ans += nums_dict[tmp_sum - k]
            
            nums_dict[tmp_sum] += 1
        print(nums_dict)
        return ans
    
# brute force // 시간 초과    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)

        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum == k:
                    ans += 1

        return ans