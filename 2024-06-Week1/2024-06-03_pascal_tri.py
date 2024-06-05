# https://www.acmicpc.net/problem/16395

import sys
input = sys.stdin.readline

# n번째 행 k 번째 수
#       1
#     1   1
#   1   2   1
# 1   3   3   1
n, k = map(int, input().split())
pascal = [[1], [1,1]]
for i in range(2,n):
    next = []
    for j in range(len(pascal[i-1])+1):
        # print("i,j", i, j)
        if j == 0 or j == len(pascal[i-1]):
            next.append(1)
        else:
            next.append(pascal[i-1][j-1]+pascal[i-1][j])
    pascal.append(next)
    # print(pascal)

print(pascal[n-1][k-1])