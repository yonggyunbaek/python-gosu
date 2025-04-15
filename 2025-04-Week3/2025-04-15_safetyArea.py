# https://www.acmicpc.net/problem/2468

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
# 입력 그래프
graph = [ list(map(int,input().split())) for _ in range(n) ]

# 상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# h는 물높이, h이하 물에 잠김
def dfs(a,b,h):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] > h:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return 

maxv = 0
for h in range(0,101):
    cnt = 0
    visited = [ [0]*n for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                dfs(i,j,h)
                cnt += 1
    maxv = max(maxv, cnt)

print(maxv)