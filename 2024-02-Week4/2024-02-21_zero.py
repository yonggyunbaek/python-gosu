# 백준 10773

import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))
