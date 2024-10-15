# https://leetcode.com/problems/find-the-maximum-achievable-number/submissions/

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t * 2)
