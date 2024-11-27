# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int,input().split()))
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
