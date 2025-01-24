import heapq
import sys
input = sys.stdin.readline

# # 한 노드에서 전체 다른 노드에 가는 최단거리 계산
# def dijkstra(start:int):
#     q = []
    
#     heapq.heappush(q, (0,start))
#     # 출발 위치 거리값 0으로 초기화
#     distance[start] = 0
    
#     while q:
#         # 출발 노드로 부터 거리 dist, 현재 노드 now
#         dist, now = heapq.heappop(q)
        
#         if distance[now] < dist:
#             continue

#         for i in graph[now]:
#             #i[0] 길/지름길 도착지점
#             #i[1] 길/지름길 길이
#             cost = dist + i[1] #현재 지점에서 길/지름길을 더함 

#             #해당 노드로 가는데 계산된 비용이 최단거리테이블보다 작으면 업데이트
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
    
# n, d = map(int,input().split())

# INF = int(1e9)
# # 0번 노드로 부터 각 노드까지의 거리를 INF로 초기화
# distance = [INF]*(d+1)
# graph = [[] for _ in range(d+1)]

# for i in range(d):
#     graph[i].append((i+1,1))

# for _ in range(n):
#     start, end , length = map(int, input().split())
    
#     if end > d: 
#         continue
    
#     #지름길 정보 입력
#     graph[start].append((end, length))


# dijkstra(0)
# print(distance[d])

n, d = map(int, input().rstrip().split(' '))

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split(' '))))

distance = [i for i in range(d+1)]

for i in range(d+1):
    # i까지의 거리는 i까지 고속도로 길이와 지름길 길이중 작은값
    distance[i] = min(distance[i], distance[i-1]+1)
    for start, end, dist in graph:
        # i가 start랑 같고 end가 고속도로 전체길이(d)보다 작고 현재까지 온 고속도로의 길이+지름길이 end까지 길이보다 짧으면 
        if i == start and end <= d and distance[i] + dist < distance[end]:
            # end까지 거리 업데이트
            distance[end] = distance[start] + dist

print(distance[d])