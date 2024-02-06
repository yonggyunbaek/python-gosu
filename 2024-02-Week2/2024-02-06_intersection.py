"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums2 = list(set(nums2))
        for n in nums2:
            if n in nums1:
                ans.append(n)
                
        return ans
    
    
"""
list를 set 형태로 변환 시, 중복된 element가 제거 됨.
"""