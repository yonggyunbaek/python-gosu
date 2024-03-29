"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
"""


# 풀이 1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y # 2진수 비교  

        print(xor)
        
        distance = 0
        while xor:
            xor &= xor - 1
            distance += 1
        
        return distance


# 풀이 2
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        
        lx = len(x_bin)
        ly = len(y_bin)
        l = max(lx,ly)
        
        sm = 0
        x_bin = '0'*(l-lx)+x_bin
        y_bin = '0'*(l-ly)+y_bin

        for i in range(l-1,-1,-1):
            if x_bin[i]!=y_bin[i]:
                sm+=1

        return sm        
        