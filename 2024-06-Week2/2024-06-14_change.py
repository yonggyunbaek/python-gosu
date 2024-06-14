# https://www.acmicpc.net/problem/14916

import sys
input = sys.stdin.readline

n = int(input())
cnt = []

if n >= 5:
    a = n // 5
    for i in range(0,a+1):
        b = n - 5*i
        if b % 2 == 0:
            cnt.append(i + b//2)
    print(min(cnt))

else:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(-1)

