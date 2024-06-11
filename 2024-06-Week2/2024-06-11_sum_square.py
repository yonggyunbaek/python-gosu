# https://www.acmicpc.net/problem/1699

import sys

input = sys.stdin.readline

n = int(input())
dp = [k for k in range(n+1)]
# dp = [0 ,1 ,2, 3, ... , n]
for i in range(1, n + 1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
            # 새로운 제곱 수가 등장할 때 i-j*j = 0 ->  dp[0] + 1 = 1
            # i = 5 라면 j = 2까지 loop 돌고 dp[5-2*2]+1 = dp[1] + 1 = 2
print(dp[n])


