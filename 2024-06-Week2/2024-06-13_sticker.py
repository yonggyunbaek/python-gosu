# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [ list(map(int,input().split())) for _ in range(2) ]
    # [[50, 10, 100, 20, 40]
    #  [30, 50, 70 , 10, 60]]

    DP = [ [0]*n for _ in range(2) ]
    # [[0, 0, 0, 0, 0]
    #  [0, 0, 0, 0, 0]]

    # n번째
    # n = 1일 경우
    DP[0][0] = sticker[0][0]
    DP[1][0] = sticker[1][0]
    if n == 1:
        print(max(DP[0][0],DP[1][0]))
        continue

    # n = 2 
    DP[0][1] = sticker[1][0] + sticker[0][1]
    DP[1][1] = sticker[0][0] + sticker[1][1]
    if n == 2:
        print(max(DP[0][1],DP[1][1]))
        continue

    # n >= 3
    # max(n-2번째 + n번째, n-1번째 + n번째)
    for i in range(2, n):
        DP[0][i] = max(DP[1][i-1], DP[1][i-2]) + sticker[0][i]
        DP[1][i] = max(DP[0][i-1], DP[0][i-2]) + sticker[1][i]

    print(max(DP[0][-1],DP[1][-1]))