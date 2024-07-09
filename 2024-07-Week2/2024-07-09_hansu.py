# https://www.acmicpc.net/problem/1065

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1,n+1):
    if i < 100:
        cnt += 1
    else:
        a = i // 100
        b = (i - 100*a) // 10
        c = i - 100*a -10*b
        if a-b == b-c:
            cnt += 1

print(cnt)