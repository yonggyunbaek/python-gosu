#  https://leetcode.com/problems/shuffle-the-array/submissions/

from collections import deque
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        queue1 = deque(nums[:n])
        queue2 = deque(nums[n:])
        
        answer = []
        while queue1:
            q1 = queue1.popleft()
            q2 = queue2.popleft()
            
            answer.append(q1)
            answer.append(q2)
            
        return answer
            
