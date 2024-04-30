"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        # print(bin(num)[2:])
        ans = []
        for b in (bin(num)[2:]):
            if b == '1':
                ans.append("0")
            else:
                ans.append("1")
        return int(''.join(ans),2)