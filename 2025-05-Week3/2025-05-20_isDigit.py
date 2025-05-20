# https://www.acmicpc.net/problem/10821

import sys
input = sys.stdin.readline

cnt = 0
for s in input().rstrip().split(","):
    if s.isdigit():
        cnt += 1

print(cnt)