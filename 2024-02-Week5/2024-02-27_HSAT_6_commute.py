# 출퇴근길
# 단방향 그래프 1 ~ n 
# n 개의 정점으로 m개의 일방통행도로를 간선으로 
# S(집) T(회사)
# S에서 T로 가는 출근길 경로와 T에서 S로 가는 퇴근길 경로에 모두 포함될 수 있는 정점의 개수를 세는 프로그램
# 출근길은 T에 도착하면 끝, S는 여러번 가능
# 퇴근길은 S에 도착하면 끝, T는 여러번 가능

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# 노드에서 나갈 수 있는 노드 번호 2차원 배열
adj = [[] for _ in range(n+1)]
# 노드로 들어올 수 있는 노드 번호 2차원 배열
adjR = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adjR[y].append(x)

S, T = map(int, input().split())


def dfs(now, adj, visited):
    if visited[now] == 1:
        return
    visited[now] = 1
    for neighbor in adj[now]:
        dfs(neighbor, adj, visited)
    return

fromS = [0]*(n+1)
fromS[T]=1 
dfs(S, adj, fromS)

fromT = [0]*(n+1)
fromT[S]=1  
dfs(T, adj, fromT)

toS = [0]*(n+1)
dfs(S,adjR,toS)

toT = [0]*(n+1)
dfs(T, adjR, toT)
           
count = 0 
for i in range(1,n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count+=1
print(count-2)