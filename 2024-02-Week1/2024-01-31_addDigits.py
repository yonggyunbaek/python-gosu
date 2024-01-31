"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while True:
            tmp = 0
            for s in str(num):
                tmp += int(s)
            if tmp < 10:
                return tmp
                break
            else:
                num = tmp
                continue
            
            
            
#without loop
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1
        
"""
num이 12 일 때,
(12 - 1) % 9 -> 2
2 + 1 = 3

num = 123
(123 - 1) % 9 -> 5
5 + 1 = 6

"""