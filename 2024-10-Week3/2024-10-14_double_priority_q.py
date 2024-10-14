# https://www.acmicpc.net/problem/7662

import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    minq = []
    maxq = []
    visited = [1] * k
    for i in range(k):
        operation = input().split()
        if operation[0] == "I":
            heapq.heappush(maxq, (int(operation[1])*-1, i))
            heapq.heappush(minq, (int(operation[1]), i))
            # print("I", q)
        else:
            if maxq and operation[1] == '1':
                visited[heapq.heappop(maxq)[1]] = 0

            elif minq and operation[1] == '-1':
                visited[heapq.heappop(minq)[1]] = 0
                # print("D -1", q)
        # print("before sync", minq,"###", maxq)
        while minq and visited[minq[0][1]] == 0:
            heapq.heappop(minq)
        while maxq and visited[maxq[0][1]] == 0:
            heapq.heappop(maxq)            
        # print("after sync", minq,"###", maxq, visited)
    
    if not minq:
        print("EMPTY")
    else:
        print(-maxq[0][0], minq[0][0])


