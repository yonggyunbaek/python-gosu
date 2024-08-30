# https://www.acmicpc.net/problem/1417

import sys
import heapq

input = sys.stdin.readline

n = int(input())
votes = [int(input()) for _ in range(n)]

# 다솜이의 득표 수
dasom = votes[0]
# 나머지 후보들의 득표 수
others = votes[1:]

# 최대힙
others = [-x for x in others]
heapq.heapify(others)

cnt = 0
while others and -others[0] >= dasom:
    max_vote = -heapq.heappop(others)
    max_vote -= 1
    dasom += 1
    cnt += 1
    heapq.heappush(others, -max_vote)

print(cnt)
