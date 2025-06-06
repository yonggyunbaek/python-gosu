# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/submissions/
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if mod := x % 3:
                ans += min(mod, 3 - mod)
        return ans
