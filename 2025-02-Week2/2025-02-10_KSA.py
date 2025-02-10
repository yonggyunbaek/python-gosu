# https://www.acmicpc.net/problem/29197

import sys
input = sys.stdin.readline

n = int(input())

quadrant1 = set()
quadrant2 = set()
quadrant3 = set()
quadrant4 = set()
axis = set()

for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y > 0 :
        axis.add('y')
    elif x == 0 and y < 0:
        axis.add('-y')
    elif x > 0 and y == 0:
        axis.add('x')
    elif x < 0 and y == 0:
        axis.add('-x')
    elif x > 0 and y > 0:
        a = y / x 
        quadrant1.add(a)
    elif x < 0 and y > 0:
        a = y / x
        quadrant2.add(a)
    elif x < 0 and y < 0:
        a = y / x
        quadrant3.add(a)
    elif x > 0 and y < 0:
        a = y / x 
        quadrant4.add(a)            

print(len(quadrant1)+len(quadrant2)+len(quadrant3)+len(quadrant4)+len(axis))