# https://www.acmicpc.net/problem/1012

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 스택으로 dfs 
def dfs(graph, a, b):
    # 방문이 필요한 노드 q
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    return graph

t = int(input())

for _ in range(t):
    m, n, k = map(int,input().split())
    graph = [ [0] * n for _ in range(m) ]
    for _ in range(k):
        a, b = map(int,input().split())
        graph[a][b] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                graph = dfs(graph,i,j)
                cnt += 1
                # print(graph)
    print(cnt)

    