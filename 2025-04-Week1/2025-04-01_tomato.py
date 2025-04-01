# https://www.acmicpc.net/problem/7576

from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph):
    maxday = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 지정
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                # 방문했으면 현재위치값 +1
                graph[nx][ny] = graph[x][y] + 1
                maxday = max(maxday, graph[nx][ny])
                q.append((nx,ny))
    return maxday

m,n = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n) ]

q = deque()
qcheck = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
        elif graph[i][j] == -1:
            qcheck.append((i, j))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if len(q) + len(qcheck) == n*m:
    print(0)
else:
    cnt = bfs(graph)

    for row in graph:
        if 0 in row:
            print(-1)
            break
    else:
        print(cnt-1)


