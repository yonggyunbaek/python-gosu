# https://www.acmicpc.net/problem/1735

import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)
    
A, B = map(int,input().split())
C, D = map(int,input().split())

tempA = (A*D) + (C*B)
tempB = (B*D)

x = gcd(tempA, tempB)
print(tempA//x, tempB//x)