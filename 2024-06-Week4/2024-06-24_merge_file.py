# https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = [0] + list(map(int, input().split()))
    # [0, 40, 30, 30, 50]
    
    # dp[i][j]는 i번째부터 j번째 까지 합치는 최솟값
    dp = [[0]*(K+1) for _ in range(K+1)]
    # print(dp)
    # 두 파일 연속이면 합
    for i in range(1,K+1):
        for j in range(1, K+1):
            if j==i+1:
                dp[i][j] == arr[i] + arr[j]
        # print(dp)

    # 밑에서 부터 올라오면서 dp 채우기
    # dp[1][4] = min(dp[1][1]+dp[2][4], dp[1][2],dp[3][4], dp[1][3]+dp[4][4])
    for i in range(K-1, 0, -1):
        for j in range(1,K+1):
            # print(i,j)
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([ dp[i][k]+dp[k+1][j] for k in range(i,j) ]) + sum(arr[i:j+1])
    print(dp[1][K])

# dp 예시
# 1
# 40 30 30 50
# 입력 시

# [[0, 0, 0, 0, 0], 
#  [0, 0, 70, 160, 300], 
#  [0, 0, 0, 60, 170], 
#  [0, 0, 0, 0, 80], 
#  [0, 0, 0, 0, 0]]