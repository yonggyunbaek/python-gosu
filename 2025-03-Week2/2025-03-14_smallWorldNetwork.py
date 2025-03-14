from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(start):
    answer = []
    # 시작점 큐삽입
    q = deque([start])
    # 시작점 방문 확인
    visited[start] = True
    # 시작점 거리 0
    distance[start] = 0
    # 앞으로 방문할 노드 있으면 
    while q:
        # 선입선출
        now = q.popleft()
        # 현재 노드에 인접한 노드 확인해서 방문체크하고 q 삽입
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                # 인접한 노드(i)를 인덱스로 리스트 값(거리) +1
                distance[i] = distance[now] + 1
    if distance[1:].count(0) > 1:
        return 4950
    return max(distance)

n, k = map(int,input().split())
graph = defaultdict(list)


for i in range(k):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

maxl = 0
for i in range(1,n+1):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    # print(bfs(i))
    maxl = max(maxl, bfs(i))

if maxl > 6:
    print("Big World!")
else:
    print("Small World!")