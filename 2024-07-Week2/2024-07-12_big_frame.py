# https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline

N = int(input())
p = [ list(map(int,input().split())) for _ in range(N)]

answer = []

for i in range(N):
    cnt = 1
    a, b = p[i][0], p[i][1]
    for j in range(N):
        
        if i != j:
            c, d = p[j][0], p[j][1]
            if a < c and b < d:
                cnt += 1
    answer.append(cnt)

print(*answer)
