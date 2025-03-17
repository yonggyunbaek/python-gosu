# https://www.acmicpc.net/problem/2644

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                # 인접한 노드(i)를 인덱스로 리스트 값(거리) +1
                distance[i] = distance[now] + 1
    return distance


n = int(input())
a, b = map(int,input().split())

m = int(input())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
distance = [ -1 ] * (n+1)

distance = bfs(a)
print(distance[b])
