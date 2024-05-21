# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q=deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or ny<0 or nx >= N or ny >= M:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx,ny))
        # print(q, maze)
    return maze[N-1][M-1]

N, M = map(int,input().split())
maze = [ list(map(int,list(input().strip()))) for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]
# print(visited)
# print(maze)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs(0,0))