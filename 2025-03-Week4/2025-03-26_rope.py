# https://www.acmicpc.net/problem/2217

import sys
import heapq
input = sys.stdin.readline

n = int(input())

weight = []
for _ in range(n):
    heapq.heappush(weight,int(input()))

cnt = 0
maxw = 0
while weight:
    w = heapq.heappop(weight)
    maxw = max(maxw, w*(n-cnt))
    cnt += 1

print(maxw)