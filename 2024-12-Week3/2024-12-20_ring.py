# https://www.acmicpc.net/problem/5555

import sys
input = sys.stdin.readline

find = input().rstrip()
n = int(input())
cnt = 0
for _ in range(n):
    ring = input().rstrip()
    if find in ring*2:
        cnt += 1

print(cnt)