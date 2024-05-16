"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        element = collections.Counter(nums)
        for e in element:
            # print(e)
            # print(element[e])
            if element[e] >= len(nums) / 2:
                return e
                