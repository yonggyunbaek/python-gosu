"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""
class Solution:
    def isUgly(self, n):
        if n == 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i

        return n == 1

## 시간 초과1
class Solution:
    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    
    def isUgly(self, n: int) -> bool:
        n = abs(n)
        if n == 1:
            return True
        
        ans = []
        for i in range(2, n + 1):
            if n % i == 0:
                if self.isPrime(i):
                    ans.append(i)
                if self.isPrime(n // i):
                    ans.append(n // i)
        
        uglynum = [2, 3, 5]
        result = [x for x in ans if x not in uglynum]
        
        if result:
            return False
        else:
            return True
        
        
## 시간 초과2
import math
class Solution:
    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    
    def isUgly(self, n: int) -> bool:
        n = abs(n)
        if n == 1:
            return True
        
        primes = [2, 3, 5]
        for prime in primes:
            while n % prime == 0:
                n //= prime
        
        return n == 1


""" 
약수 구하는 방법 2가지
1. O(N)
List = []

for i in range(1, n + 1):
    if (n % i == 0) :
        List.append(i)
        
2. O(N^(1/2))
List = []

for i in range(1, int(n**(1/2)) + 1):
    if (n % i == 0):
        divisorsList.append(i) 
        if ( (i**2) != n) : 
            divisorsList.append(n // i)
"""