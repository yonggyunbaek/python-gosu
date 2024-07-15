# https://www.acmicpc.net/problem/15903

import sys
import heapq
input = sys.stdin.readline

# n개 m번
n, m = map(int,input().split())
card = list(map(int,input().split()))
heapq.heapify(card)

for _ in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    heapq.heappush(card, a+b)

print(sum(card))