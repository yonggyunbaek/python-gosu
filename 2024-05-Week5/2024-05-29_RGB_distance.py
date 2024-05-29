# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int,input().split())))

answer = [ [0]*3 for _ in range(N+1) ]

# print(dp, answer)

for i in range(1,N+1):
    answer[i][0] = min(answer[i-1][1], answer[i-1][2]) + dp[i-1][0]
    answer[i][1] = min(answer[i-1][0], answer[i-1][2]) + dp[i-1][1]
    answer[i][2] = min(answer[i-1][0], answer[i-1][1]) + dp[i-1][2]

print(min(answer[N]))