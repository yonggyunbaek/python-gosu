"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

# 풀이 1 / 시간초과
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []        
        for f in range(1,len(nums)+1):
            
            if f not in nums:
                ans.append(f)
                
        return ans

# 풀이 2
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_list = [i for i in range(1,len(nums)+1)]
        return list(set(full_list) - set(nums)) 
    
    
# 풀이 3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]