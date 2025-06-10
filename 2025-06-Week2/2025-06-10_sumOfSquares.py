# https://www.acmicpc.net/problem/1699

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 100001
# dp[n]은 n을 제곱수의 합으로 만들때 항의 최소개수
# 제곱수를 빼보면서 항의 최소개수를 찾는다

# dp[1] = 1
# dp[2] = min(1**2 빼보면 1 남고 dp[1] = 1 이러면 항개수 2) = 2
# dp[3] = min(1**2 빼보면 2 남고 dp[2] = 2 이러면 항개수 3) = 3
# dp[4] = min(1**2 빼보면 3 남고 dp[3] = 3 이러면 항개수 4, 2**2 빼보면 0이고 항개수는 1 ) = 1
# dp[5] = min(1**2 빼보면 4 남고 dp[4] = 1 이러면 항개수 2, 2**2 빼보면 1남고 dp[1] = 1 이면 항개수 2) = 2
# dp[6] = min(1**2 빼보면 5 남고 dp[5] = 2 이러면 항개수 3, 2**2 빼보면 2남고 dp[2] = 2 이면 항개수 3) = 2
# ...
# dp[9] = 1
# dp[10] = min(1**2 빼보면 9남고 dp[9] = 1 이러면 항개수 2, 2**2 빼보면 6남고 dp[6] = 2 이면 항개수 3, 3**3빼보면 dp[1] = 1 이면 항개수 2) = 2

for i in range(1, n+1):
    # i가 제곱수면
    if (i**0.5)%1 == 0:
        dp[i] = 1
    else:
        minv = 1e9
        # j는 1부터 i의 제곱근 까지의 수
        for j in range(1, int(i**0.5)+1): 
            minv = min(minv, dp[i-j**2])
        dp[i] = minv+1

print(dp[n])