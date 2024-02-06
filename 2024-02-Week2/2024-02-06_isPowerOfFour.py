"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 4:
            return False
        
        
        ans = int(round(math.log(n,4)))
        if n == 4**ans:
            return True
        else:
            return False