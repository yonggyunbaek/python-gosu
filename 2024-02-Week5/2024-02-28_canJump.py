"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

# 풀이1 / 타임아웃 BFS 알고리즘
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        stack = [[0,nums[0]]] # index, sum
        
        while stack:
            index, jump_len = stack.pop(0)
            # print(index, jump_len, "**")
            
            for i in range(1,jump_len+1):
                new_index = index + i#0+1
                new_jump_len = nums[new_index]
                print(new_index,new_jump_len)
                
                if new_index == len(nums) - 1:
                    # print(new_index,len(nums), "@@@")
                    return True
                
                stack.append([new_index,new_jump_len])
        return False

# 풀이2 
class Solution(object):
    def canJump(self, nums):
        jump_length = nums[0]
        
        for i in range(1,len(nums)):
            if jump_length == 0:
                return False
            jump_length -= 1
            
            jump_length = max(jump_length, nums[i])
            print(i,nums[i],jump_length)
        return True

# 풀이3 / 그리디 알고리즘

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i, length in enumerate(nums):
            if i > reachable:
                return False
            reachable = max(reachable, i + length)
        return True
    
"""
그리디 알고리즘
최적의 해를 구하는 알고리즘
>> 각 단계에서 가장 이상적인 선택을 하는 것이 전체적으로 최적의 결과를 가져온다는 것
"""