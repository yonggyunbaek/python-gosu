# https://www.acmicpc.net/problem/2458

from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def dfs(now, idx):
    for node in height[idx]: # 나보다 큰 친구들 순회
        if visited[now][node] == 0: # 아직 확인 안한 친구면
            visited[now][node] = 1 # now 보다 크다고 표시
            visited[node][now] = 1 # 상대 친구한테 나보다 작다고 아는 것을 표시
            dfs(now, node) # 방금 확인한 나보다 큰 애보다 더 큰 애 찾아

n, m = map(int,input().split())
height = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    height[a].append(b) 

print(height)
visited = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    visited[i][i] = 1
    dfs(i,i)
    print(visited)

cnt = 0

for i in range(1, n+1):
    if sum(visited[i]) == n:
        cnt += 1

print(cnt)