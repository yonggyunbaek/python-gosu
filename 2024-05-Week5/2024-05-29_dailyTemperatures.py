"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. brute force // for loop * 2 >> Time Limit Exceeded
        """
        2중 for문 검색
        더 높은 온도일 때 ans.append() / 높은 온도, 빠른 일자 
        더 높은 온도가 없으면 ans.append() : for loop 끝까지.
        """
        ans = []
        for i in range(len(temperatures)):
            day = 0

            for j in range(i,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    day = j-i
                    break
                
            ans.append(day)

        # print(ans)
        return ans
    
    
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 2. stack, enumerate 활용
        
        ans = [0] * len(temperatures)
        stack = []
        
        for index, temp in enumerate(temperatures):
            # print(index, temp)
            while stack and temperatures[stack[-1]] < temp:
                a = stack.pop()
                ans[a] = index - a
                
            stack.append(index)
        
        return ans