# https://www.acmicpc.net/problem/2866

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

answer = []  
queue = deque()

for i in range(1, n + 1):
    queue.append(i)
# queue [1, 2, 3, 4, 5, 6, 7]

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<", end="")
print(", ".join(map(str, answer)), end="")
print(">")

