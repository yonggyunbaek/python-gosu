"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix)==1:
            return matrix[0]
        
        ans=[]
        stack = matrix.copy()
        
        while stack:
            tmp = stack.pop(0)
            for t in tmp:
                ans.append(t)
            if len(stack)==0:
                break 
                
            if len(stack)>=2:
                for s in range(len(stack)):    
                    ans.append(stack[s].pop(-1))                    
                while [] in stack:
                    stack.remove([])
            else:
                print(stack)
                tmp = reversed(stack.pop())         
                for t in tmp:
                    ans.append(t)
            
            if len(stack)==0:
                break
            tmp = reversed(stack.pop())
            for t in tmp:
                ans.append(t)
            # print(stack)
            if len(stack)>=2:
                for s in range(len(stack)-1,0,-1):
                    ans.append(stack[s].pop(0))
                while [] in stack:
                    stack.remove([])
            else:
                tmp = stack.pop()
                for t in tmp:
                    ans.append(t)
                    
        return ans
    
    
"""
리스트 정렬하는 방법.

a = sorted() : 출력이 정렬 (요소의 오름,내림차순 정렬)
sort() : 리스트 자체가 바뀜

reverse=True 옵션은 역순 정렬이 아니라 내림차순임!!


따라서, index 자체의 역순 정렬하려면
reverse()
reversed() 사용

차이는 sort(),sorted()와 같음
"""