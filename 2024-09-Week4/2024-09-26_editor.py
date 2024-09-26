# https://www.acmicpc.net/problem/1406

import sys
from collections import deque
input = sys.stdin.readline

word = deque(input().rstrip())
m = int(input())
stack = deque()

for _ in range(m):
    cmd = input().split()
    c = cmd[0]
    if c == "L" and word:
        stack.appendleft(word.pop())
    elif c == "D" and stack:
        word.append(stack.pop())
    elif c == "B" and word:
        word.pop()
    else:
        word.append(cmd[1])
    # print(word, stack)
print(''.join(word)+''.join(stack))


