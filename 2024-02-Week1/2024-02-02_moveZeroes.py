"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        while 0 in nums:
            nums.remove(0)
            zero.append(0)
        nums += zero
        

"""
1. remove()
list에서 remove를 사용하면 가장 좌측부터 첫뻔째 element 제거
괄호 안에는 element 작성

2. pop()
list에서 괄호 안의 index를 찾아 제거, 값 반환 가능
index 업을 시, 마지막 element 제거 및 반환
ex) value = list.pop()

3. del list
del은 pop과 다르게 element를 반환하지는 않음. 하지만 범위로 제거 가능
ex) del exam_list[3:5]  // 3~5 번째 리스트 요소 제거
"""