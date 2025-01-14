# https://www.acmicpc.net/problem/1002
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    r = (r1+r2)
    # print(d ,r1+r2)
    if d == 0:
        if r1 != r2:
            print(0)
        else:
            print(-1)
    else:
        # 내접하는 경우도 고려
        if d == r or d == abs(r1-r2):
            print(1)
        elif abs(r1-r2) < d < r:
            print(2)
        else:
            print(0)


