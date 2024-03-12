# https://softeer.ai/practice/6291

import sys
import heapq
input = sys.stdin.readline

N = int(input())
time_lst = []

for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(time_lst,(b,a))

answer = 0
now = 0

while time_lst:
    a, b = heapq.heappop(time_lst)
    if b >= now:
        answer += 1
        now = a

print(answer)