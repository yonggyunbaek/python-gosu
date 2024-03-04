"""
57. Insert Interval
Medium

9534

720

Add to List

Share
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

# 풀이 1 /성공
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        interval_stack = intervals.copy()
        left, right = newInterval[0], newInterval[1]
        ans = []
        
        while interval_stack:
            new_left, new_right = interval_stack.pop(0)
            
            if new_right < newInterval[0]:
                ans.append([new_left, new_right])
                continue
            
            elif new_left > newInterval[1]:
                ans.append([new_left, new_right])
                continue
            
            else:
                left = min(new_left, left)
                right = max(new_right, right)
                
        ans.append([left,right])
        ans.sort()
        
        return ans

#풀이 2 /실패

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]
        
        interval_stack = intervals.copy()
        left, right = newInterval[0], newInterval[1]
        ans = []
        for i in range(2):
            if i == 0:
                while interval_stack:
                    new_left, new_right = interval_stack.pop(0)
                    
                    if new_right < newInterval[i]:
                        ans.append([new_left, new_right])
                    elif new_left <= newInterval[i] <= new_right:
                        left = new_left
                        break

                # print(ans, left, right)
            else:# i==1
                while interval_stack:
                    new_left, new_right = interval_stack.pop(0)
                    
                    if new_right < newInterval[i]:
                        right = newInterval[i]
                    elif new_left <= newInterval[i] <= new_right:
                        ans.append([left,new_right])
                        break
                    elif newInterval[i] < new_left:
                        ans.append([left,right])
                        ans.append([new_left,new_right])
                        break
                # print(ans, left, right)
        while interval_stack:
            val = interval_stack.pop(0)
            ans.append(val)
        
        return ans
"""
리스트 내의 크기 비교를 해서 값을 정하는 것은 min, max를 우선적으로 생각해보자....

"""