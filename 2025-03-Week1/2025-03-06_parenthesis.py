# https://www.acmicpc.net/problem/11899

from collections import deque
import sys
input = sys.stdin.readline

parenthesis = list(input().rstrip())
queue = deque()

for i in parenthesis:
    if not queue:
        queue.append(i)
    elif queue[-1] == "(" and i == ")":
        queue.pop()
    else:
        queue.append(i)

print(len(queue))