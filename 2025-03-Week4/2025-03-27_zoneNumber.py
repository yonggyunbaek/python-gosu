# https://www.acmicpc.net/problem/2667

from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    # 1 지점부터 탐색 시작
    q.append((a,b))
    # 방문한 지점 0으로
    graph[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 지정
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                # 방문했으면 0으로
                graph[nx][ny] = 0
                q.append((nx,ny))
                count += 1
    # q 비어서 while 벗어나면 1로 이어지는 구역 탐색 끝
    return count

n = int(input())
graph = [ list(map(int,input().rstrip())) for _ in range(n) ]

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph,i,j))

cnt.sort()
print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])