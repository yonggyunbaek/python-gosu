# https://www.acmicpc.net/problem/2295

import sys
input = sys.stdin.readline

n = int(input())
arr = sorted((int(input()) for _ in range(n)))

sumOfTwoNums = set()
for i in range(n):
    for j in range(i,n):
        sumOfTwoNums.add(arr[i]+arr[j])

# arr에서 큰 수 부터 2개씩 차이 계산 해서 두수의 합이 저장된 리스트에 있는지 확인
flag = 0
for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if arr[i] - arr[j] in sumOfTwoNums:
            print(arr[i])
            flag = 1
            break
    if flag == 1:
        break


# 세 수의 합 전 경우의 수(중복 포함) n^3
# 두 수의 합(중복 포함) n^2 + 두 수의 차(중복 x) n^2