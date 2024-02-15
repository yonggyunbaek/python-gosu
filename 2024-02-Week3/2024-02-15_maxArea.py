"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
# 풀이 1 / 시간초과
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        self.height = height
        # height를 얻고 비교합니다.
        for l in range(len(height)-1):
            for r in range(1, len(height)):
                tmp = self.getHeight(l, r)
                if tmp > ans:
                    ans = tmp
        return ans
    
    def getHeight(self, left: int, right: int) -> int:
        cur_height = (right - left) * min(self.height[right], self.height[left])
        return cur_height

# 풀이 2 / 패스
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            cur_height = min(height[left], height[right])
            cur_width = right - left
            cur_area = cur_height * cur_width
            ans = max(ans, cur_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans
