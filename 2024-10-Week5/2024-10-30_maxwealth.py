# https://leetcode.com/problems/richest-customer-wealth/description/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for a in accounts:
            if max_wealth < sum(a):
                max_wealth = sum(a)

        return max_wealth