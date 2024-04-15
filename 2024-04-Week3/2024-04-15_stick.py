# https://www.acmicpc.net/problem/17608

import sys
input = sys.stdin.readline

N = int(input())

stick = [ int(input()) for _ in range(N) ]
c = 0
cnt = 0
for _ in range(N):
    threshold = stick.pop()
    if threshold > c:
        c = threshold
        cnt += 1

    else:
        continue
print(cnt)