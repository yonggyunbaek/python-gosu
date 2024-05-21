"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        for n in range(len(nums)+1):
            # print(list(map(list,itertools.combinations(nums,n))))
            for a in list(map(list,itertools.combinations(nums,n))):
                ans.append(a)
            
        # print(ans)
        return ans