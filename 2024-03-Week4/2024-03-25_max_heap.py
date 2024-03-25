# https://www.acmicpc.net/problem/11279

import sys
import heapq

input = sys.stdin.readline

N = int(input())
numlst = []

for _ in range(N):
    v = int(input())
    if v == 0:
        if len(numlst) == 0:
            print(0)
        else:
            # -붙여서 만들어진 numlst에서 heappop하면 제일 작은 음수값 나오니까 -붙여서 출력하면 최대값
            print(-heapq.heappop(numlst))
    else:
        # 최대힙 구현하도록 값을 넣을 때 -붙여서
        heapq.heappush(numlst, -v)