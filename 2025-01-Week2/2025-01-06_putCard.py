# https://www.acmicpc.net/problem/18115

import sys
from collections import deque
input =sys.stdin.readline

N = int(input())
skill = list(map(int, sys.stdin.readline().split()))
skill.reverse()

dq = deque()
for i in range(N):
    if skill[i] == 1:
        dq.appendleft(i + 1)
    elif skill[i] == 2:
        dq.insert(1, i + 1)
    elif skill[i] == 3:
        dq.append(i + 1)

for i in dq:
    print(i, end=" ")