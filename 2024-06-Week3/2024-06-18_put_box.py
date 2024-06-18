# https://www.acmicpc.net/problem/1965

import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # print(i,j)
        # 증가하는 값이면
        if box[i] > box[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        # print(dp)

print(max(dp))

# LIS, Longest Increasing Subsequence
# 죄장 증가 부분 수열
