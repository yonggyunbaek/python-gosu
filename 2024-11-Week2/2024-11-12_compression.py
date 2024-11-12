# https://www.acmicpc.net/problem/1662

import sys
from collections import deque

input = sys.stdin.readline

inputStr = list(input().rstrip())
input_stack = []
length = 0
iter_num = 0
for s in inputStr:
    if s.isdigit():
        length += 1
        iter_num = s
    elif s == "(":
        input_stack.append([int(iter_num), length - 1])
        length = 0
    else:
        multi, pre_left = input_stack.pop()
        length = ((multi * length) + pre_left)
    print(s, iter_num, length, input_stack)
print(length)
