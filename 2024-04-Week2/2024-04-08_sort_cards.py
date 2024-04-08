# https://www.acmicpc.net/problem/1715

import sys
import heapq
input = sys.stdin.readline

N = int(input())
numlst = []
for _ in range(N):
    k = int(input())
    heapq.heappush(numlst, k)

cnt = 0
while len(numlst) > 1:
    # print(numlst)
    # print(cnt)
    a = heapq.heappop(numlst)
    b = heapq.heappop(numlst)
    cnt += a
    cnt += b
    heapq.heappush(numlst, a+b)

print(cnt)