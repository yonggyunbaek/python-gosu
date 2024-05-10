# https://www.acmicpc.net/problem/11650

import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    x, y = map(int,input().split())
    heapq.heappush(q,[x,y])
# print(q)
for _ in range(N):
    A = heapq.heappop(q)
    print(A[0], A[1])