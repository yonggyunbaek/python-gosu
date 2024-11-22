# https://www.acmicpc.net/problem/4889

import sys
from collections import deque, Counter
input = sys.stdin.readline
idx = 0
while True:
    stack = deque()
    idx += 1
    testcase = list(input().rstrip())
    if '-' in testcase: 
        break
    cnt = 0
    for i in testcase:
        if i == '{':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                cnt += 1
                stack.append(i)
        # print(stack, cnt)
    cnt += len(stack)//2
    print(f'{idx}. {cnt}')
