# https://www.acmicpc.net/problem/1927

import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = [ ]
for _ in range(N):
    v = int(input())
    if v == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, v)
