# https://www.acmicpc.net/problem/2022


import sys
from math import sqrt
input = sys.stdin.readline

x, y, c = map(float, input().split())
start, end = 0, min(x,y)

def get_c(mid):
    a = sqrt(x**2 - mid**2)
    b = sqrt(y**2 - mid**2)
    return a*b/(a+b)

result = 0

while end-start > (10**(-6)):
    mid = (start+end) / 2
    if get_c(mid) >= c:
        result = mid
        start = mid
    else:
        end = mid

# print("{}".format(round(result, 3)))
print("%.3f" %(result))