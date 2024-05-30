# https://www.acmicpc.net/problem/11052


import sys
input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

ans = []

# dp[i] = 카드 i개 구매하는 최대 가격
# card[k] = k개가 들어있는 카드팩 가격
for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + card[k])
        # print(dp)

        
print(dp[n])
