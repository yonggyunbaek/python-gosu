# https://www.acmicpc.net/problem/2583
from collections import deque
import sys
input = sys.stdin.readline

def color(a,b,c,d):
    for i in range(b,d):
        for j in range(a,c):
            graph[i][j] = 0
    return graph

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    q = deque()
    graph[x][y] = 0
    q.append((x,y))
    cnt = 1
    while q:
        nowx, nowy = q.popleft()
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if nextx >= m or nextx < 0 or nexty >=n or nexty < 0:
                continue
            if graph[nextx][nexty] == 1:
                q.append((nextx, nexty))
                graph[nextx][nexty] = 0
                cnt += 1
    return cnt

m,n,k = map(int,input().split())

graph = [ [1]*n for _ in range(m) ]

for _ in range(k):
    a,b,c,d = map(int,input().split())
    graph = color(a,b,c,d)

count = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(dfs(i,j))
print(len(count))
print(*sorted(count))