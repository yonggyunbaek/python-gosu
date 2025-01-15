# https://www.acmicpc.net/problem/1004

import sys
input = sys.stdin.readline

# 두 점 사이 거리
def distance(a, b, c, d):
    return abs( (((a-c)**2) + ((b-d)**2))**0.5 )

t = int(input())

for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        c1, c2, r = map(int,input().split())

        d1 = distance(c1, c2, x1, y1)
        d2 = distance(c1, c2, x2, y2)        
        if d1 < r and d2 > r:
            cnt += 1
        if d2 < r and d1 > r:
            cnt += 1
        # print(d1, d2, r, cnt)
    print(cnt)