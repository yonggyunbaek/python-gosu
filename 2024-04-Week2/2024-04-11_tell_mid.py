# https://www.acmicpc.net/problem/1655

import sys
import heapq
input = sys.stdin.readline

lowerthanmid = []
higherthanmid = []

N = int(input())
for _ in range(N):
    k = int(input())
    
    if len(lowerthanmid) == len(higherthanmid):
        heapq.heappush(lowerthanmid, -k) # 중간보다 작은값들 최대힙
    else:
        heapq.heappush(higherthanmid, k) # 중간보다 큰값들 최소힙
    print("low",lowerthanmid)
    print("high",higherthanmid)
    if not higherthanmid:
        print(-lowerthanmid[0])
        continue

    if -lowerthanmid[0] > higherthanmid[0]: # 최대힙(중간보다 작은값들)에서 제일 큰값이 최소힙(중간보다 큰값들)에서 가장 작은값보다 크면
        n = -heapq.heappop(lowerthanmid)    
        m = heapq.heappop(higherthanmid)
        heapq.heappush(lowerthanmid, -m)    # 최대힙에서 제일 큰값을 최소힙쪽으로
        heapq.heappush(higherthanmid,n)     # 최소힙에서 제일 작은값을 최대힙쪽으로
        print("low2",lowerthanmid)
        print("high2",higherthanmid)
    print(-lowerthanmid[0]) # 최대힙에 개수가 많게 해놓고 최대힙에서 최대값 출력, 전체 개수가 짝수여도 중간 2개중에 작은값


