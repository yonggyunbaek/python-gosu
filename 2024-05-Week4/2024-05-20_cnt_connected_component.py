# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (N+1)
for i in range(1,N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
# dfs 돌면서 방문 다 하면 return값 없이 빠져나오고 dfs 안에서 for문 끝나면  cnt += 1 하고 바깥 for문 - 다음 정점 부터 다시 확인
print(cnt)
