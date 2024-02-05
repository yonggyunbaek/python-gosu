"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

3의 제곱거듭 수인지 판별하기
"""

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 3:
            return False
        power = int(round(math.log(n, 3))) # 소수버림.
        if 3 ** power == n:
            return True
        else:
            return False
        
        
        
        
"""
어떤 자연수의 제곱거듭 판별을 하기 위한 방법.
2의 경우에는 n & (n-1) == 0 이라는 조건식으로 판별이 가능
2 = 10, 4 = 100 8 = 1000
1 = 01, 3 = 011 7 = 0111 이므로 비트연산자 and를 사용하면 0이 반환되어야 함. 2의 제곱거듭이면...

단, 위의 경우는 2의 경우에만 적용 가능, 그 외에는 log를 이용

math.log를 이용해 판별하며, math.log(n, 3)이 정수(자연수)가 아니면 사실 거듭제곱이 성립되지 않음.

math.log에서 2번째 인자를 생략시 ln(x) 가 기본.
"""