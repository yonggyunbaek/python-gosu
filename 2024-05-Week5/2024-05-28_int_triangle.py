# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int,input().split())))

# i는 층수
for i in range(1,n):
    # j는 층마다 인덱스
    for j in range(i+1):
        # 첫 원소끼리는 겹치는게 없으니 더하면 됨
        if j == 0:
            dp[i][j] += dp[i-1][j]
        # 맨 마지막 원소도 겹치는게 없으니 더하면 됨
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        # 중간 겹치는 원소는 둘 중 큰값으로 더해줌
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))

