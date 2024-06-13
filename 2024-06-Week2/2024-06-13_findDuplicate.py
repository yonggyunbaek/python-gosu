"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_nums = Counter(nums)

        return count_nums.most_common(1)[0][0]
    
    
from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n_dict = defaultdict(int)
        
        for n in nums:
            n_dict[n] += 1
            
        n_dict = sorted(n_dict.items(), reverse=True, key = lambda item: item[1])
        # print(n_dict)
        
        return n_dict[0][0]