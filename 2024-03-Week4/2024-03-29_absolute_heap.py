# https://www.acmicpc.net/problem/11286

import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    v = int(input())
    if v == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(v), v))
