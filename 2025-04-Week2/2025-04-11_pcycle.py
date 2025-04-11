# https://www.acmicpc.net/problem/10451

from collections import deque
import sys
input = sys.stdin.readline

def dfs(j):
    q = deque()
    q.append(j)
    while q:
        now = q.pop()
        if visited[now] == 0:
            visited[now] = 1
            q.append(graph[now])
    return

t = int(input())
for _ in range(t):
    n = int(input())
    cycle = list(map(int,input().split()))
    sortc = sorted(cycle)
    graph = {}
    for i in range(n):
        graph[sortc[i]] = cycle[i]
    
    visited = [0] * (sortc[-1]+1)
    cnt = 0
    for j in sortc:
        if visited[j] == 0:
            dfs(j)
            cnt += 1
    print(cnt)