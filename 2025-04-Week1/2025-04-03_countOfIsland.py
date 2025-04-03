# https://www.acmicpc.net/problem/4963

from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def dfs(graph, a, b):
    # 방문이 필요한 노드 q
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    while q:
        x, y = q.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    return graph

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    else:
        graph = [ list(map(int,input().split())) for _ in range(h)]
        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    graph = dfs(graph, i, j)
                    cnt += 1
        print(cnt)
