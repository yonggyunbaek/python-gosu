"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Follow up: Could you solve it without loops/recursion?
### 반복 루프, 회귀를 사용하지 않고 풀이할 것!
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n&(n-1) == 0:
            return True
        else:
            return False
        
        
        
# 풀이
"""
& (비트연산자)를 사용해서 풀이 가능
2 > 10
4 > 100
8 > 1000

2-1 > 01
4-1 > 011
8-1 > 0111

따라서 & 연산자를 사용하면, 출력이 0
"""