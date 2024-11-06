# https://leetcode.com/problems/number-of-employees-who-met-the-target/submissions/
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        answer = 0
        
        for h in hours:
            if h >= target:
                answer += 1
                
        return answer
