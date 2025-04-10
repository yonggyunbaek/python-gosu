# https://www.acmicpc.net/problem/14940

from collections import deque
import sys
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 지정
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                # 방문했으면 현재위치값 +1
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    return graph

n, m = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [0]*m for _ in range(n) ]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == 0:
            graph = bfs(graph,i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])