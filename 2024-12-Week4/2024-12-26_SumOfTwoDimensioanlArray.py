# https://www.acmicpc.net/problem/2167

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ar = [ list(map(int,input().split())) for _ in range(n) ]
k = int(input())

for _ in range(k):
    i, j, x, y = map(int,input().split())
    answer = 0
    for a in range(i-1,x):
        answer += sum(ar[a][j-1:y])
    print(answer)
