# https://www.acmicpc.net/problem/17298

import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
NGE = [-1] * n
stack = deque([0])

for i in range(1,n):
    while stack and a[stack[-1]] < a[i]:
        NGE[stack.pop()] = a[i]
    stack.append(i)

print(*NGE)
