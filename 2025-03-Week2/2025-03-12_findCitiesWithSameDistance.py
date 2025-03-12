# https://www.acmicpc.net/problem/18352

from collections import deque
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
                # 원하는 거리면 answer에 추가
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# distance 인덱스가 노드, 인덱스에 해당하는 값이 거리
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)