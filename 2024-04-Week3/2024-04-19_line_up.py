# https://www.acmicpc.net/problem/2605

import sys
from collections import deque
input = sys.stdin.readline

q= deque()
n = int(input())
draw = list(map(int,input().split()))

for i in range(1,n+1):
    if i == 1:
        q.append(i)
    else:
        idx = len(q) - draw[i-1]
        q.insert(idx,i)

for i in q:
    print(i, end=" ")
