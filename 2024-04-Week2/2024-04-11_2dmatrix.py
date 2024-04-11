"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""

# O(N)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in matrix:
            if target in m:
                return True
            
        return False

#O(log(N))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n*m - 1
        while left <= right:
            mid = (left + right)//2
            num = matrix[mid//m][mid%m]
            if num == target:
                return True
            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False