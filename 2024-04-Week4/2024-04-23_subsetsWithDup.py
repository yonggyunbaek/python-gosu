"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        
        def dfs(start, path, ans):
            ans.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path + [nums[i]], ans)
        
        nums.sort()
        
        dfs(0, [], ans)
        return ans