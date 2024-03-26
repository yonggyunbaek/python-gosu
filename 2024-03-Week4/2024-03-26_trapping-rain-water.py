"""
https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

# two pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:# list에 값 없을 때
            return 0
        
        volume = 0 # 빗물 양
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:# left와 right 크기 비교해서 양쪽에 index가 움직임
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                # 이전 기둥보다 작으면 그 차이만큼 물이 차 있음, 해당 차이만큼 더함
                # print(f'left side : {volume} += {left_max} - {height[left]}')
                volume += left_max - height[left]
                left += 1
            else: # left_max > right_max
                # 
                # print(f'right side : {volume} += {right_max} - {height[right]}')
                volume += right_max - height[right]
                right -= 1
                
        return volume
    
# stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):#height index
            # 높이가 꺾이는 부분(이전 height의 index보다 높이가 낮아 졌을 때)
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):# stack에 1개만 있으면 while loop break
                    break
                
                # 이전 기둥과의 높이 차이(물높이)
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
                
            stack.append(i)
        return volume