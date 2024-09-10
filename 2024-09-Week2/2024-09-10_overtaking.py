# https://www.acmicpc.net/problem/2002

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q= deque()
cnt = 0

for i in range(n):
    q.append(input().rstrip())


for i in range(n):
    out = input().rstrip()
    if out != q[0]:
        cnt += 1
        q.remove(out)
    else:
        q.popleft()

print(cnt)

