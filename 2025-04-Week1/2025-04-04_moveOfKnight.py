# https://www.acmicpc.net/problem/7562

from collections import deque
import sys

input = sys.stdin.readline

dx = [2, 1, 2, -1, -1, -2, -2, 1]
dy = [1, 2, -1, 2, -2, -1, 1, -2]

def bfs(graph,a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    while q:
        x, y = q.popleft()   
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 지정
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if graph[nx][ny] != 0:
                continue
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
            if nx == c and ny == d:
                return graph[x][y] + 1
    return 

t = int(input())

for _ in range(t):
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    a, b = map(int,input().split())
    c, d = map(int,input().split())
    if a == c and b == d:
        print(0)
    else:
        print(bfs(graph, a, b))
    

    
