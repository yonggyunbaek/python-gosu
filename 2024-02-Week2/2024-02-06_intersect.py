"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums2:
            if n in nums1:
                ans.append(n)
                nums1.remove(n)
                
        return ans

"""
list의 element 제거

remove, pop, del
"""