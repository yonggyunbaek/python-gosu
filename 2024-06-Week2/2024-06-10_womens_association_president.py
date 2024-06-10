# https://www.acmicpc.net/problem/2775

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    answer = [[1]*n for _ in range(k+1)]
    # print(answer)
    answer[0] = [ i for i in range(1,n+1) ]
    # print(answer)
    for i in range(1,k+1):
        for j in range(1,n):
            answer[i][j] = answer[i-1][j] + answer[i][j-1]
    # print(answer)
    print(answer[k][n-1])
