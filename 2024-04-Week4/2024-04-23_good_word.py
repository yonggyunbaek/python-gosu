# https://www.acmicpc.net/problem/3986

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

cnt = 0
for _ in range(N):
    word = input().strip()
    check = deque()
    for i in word:
        if not check:
            check.append(i)
        elif check[-1] == i:
            check.pop()
        else:
            check.append(i)
    if not check:
        cnt += 1
    else:
        continue

print(cnt)