# https://www.acmicpc.net/problem/14405

import sys
input = sys.stdin.readline

s = input().rstrip()
if len(s.replace('pi', ' ').replace('ka', ' ').replace('chu', ' ').replace(" ", "")) != 0:
    print('NO')
else:
    print('YES')
