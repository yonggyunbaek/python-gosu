# https://www.acmicpc.net/problem/1446

import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, distance):
    q =[]
    heapq.heappush(q, (0,start))
    distance[start] = 0
    # 큐에 값이 있으면
    while q:
        # 팝
        dist, now = heapq.heappop(q)

        # 팝해서 나온 dist가 now 까지 가는 최소비용이 아닐 수 있으니 
        # dist랑 distance[now] 비교해서 이미 더 작은 값이면 continue
        if dist > distance[now]:
            continue
        # dist가 더 작으면
        for i in graph[now]:
            cost = dist + i[1]


n, d = map(int,input().split())
graph = [[] for _ in range(d+1)]
INF = int(1e9)
distance = [INF] * (d+1)