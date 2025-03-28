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
    count = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                count += 1
    return count

n = int(input())
graph = [ list(map(int,input().rstrip())) for _ in range(n) ]

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(dfs(graph,i,j))

cnt.sort()
print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])