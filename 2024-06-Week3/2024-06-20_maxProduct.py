"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        max_so_far = nums[0]
        min_so_far = nums[0]
        ans = max_so_far

        for i in range(1, n):
            cur_num = nums[i]
            temp_max = max(cur_num, max_so_far * cur_num, min_so_far * cur_num)
            min_so_far = min(cur_num, max_so_far * cur_num, min_so_far * cur_num)

            max_so_far = temp_max
            ans = max(ans, max_so_far)

        return ans
