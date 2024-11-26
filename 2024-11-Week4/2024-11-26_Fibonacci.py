# https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
print(fibonacci(n))


# 메모이제이션 예시
# def fibonacci(n, memo={}):
#     if n in memo:
#         return memo[n]  # 이미 계산된 값이 있으면 그것을 반환
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)  # 계산한 값을 저장
#         return memo[n]