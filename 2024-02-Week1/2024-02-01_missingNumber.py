""""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""
# 풀이 1
class Solution:
    def missingNumber(self, nums: List[int]):
        nums.sort()
        for i in range (0,nums[-1]+1):
            if i not in nums:
                return i
            else:
                continue
        return len(nums)

# 풀이 2
class Solution:
    def missingNumber(self, nums: List[int]):
        n = len(nums)
        expected_sum = n * (n + 1) // 2  
        actual_sum = sum(nums)
    
        return expected_sum - actual_sum