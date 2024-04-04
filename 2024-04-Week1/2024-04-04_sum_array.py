# https://www.acmicpc.net/problem/2143

import sys
import bisect

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


#누적합 리스트생성
An = []
Bn = []

for i in range(n):
    for j in range(i+1, n+1):
        An.append(sum(A[i:j]))

for i in range(m):
    for j in range(i+1, m+1):
        Bn.append(sum(B[i:j]))

An.sort()
Bn.sort()
cnt = 0

for i in An:
    # if i >= T:
    #     break
    v = T - i 
    left = bisect.bisect_left(Bn, v)
    right = bisect.bisect_right(Bn, v)
    cnt += (right-left)

print(cnt)

'''
정렬된 리스트 에서 이진탐색 
A = [ 1, 2, 2, 3 ]

bisect_left(A,2) -> 1  # 2가 삽입되어야할 가장 왼쪽 인덱스
bisect_right(A,2) -> 3 # 2가 삽입되어야할 가장 오른쪽 인덱스
'''