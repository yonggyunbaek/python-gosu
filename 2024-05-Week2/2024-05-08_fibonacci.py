"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

class Solution:
    def fib(self, n: int) -> int:

        if n < 2:
            return n
        elif n == 2:
            return 1
        else:
            a = 0
            b = 1
            for _ in range(n):
                a,b = b, a+b

            return a