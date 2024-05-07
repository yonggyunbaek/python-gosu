# https://www.acmicpc.net/problem/2075

import sys
import heapq

input = sys.stdin.readline
q = []

N = int(input())
for _ in range(N):
    for i in map(int, input().split()):
        heapq.heappush(q, i)
        if len(q) > N:
            heapq.heappop(q)
        
print(heapq.heappop(q))