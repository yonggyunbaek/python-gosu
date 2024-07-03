# https://www.acmicpc.net/problem/1240

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

def bfs(start,end):
    q = deque()
    # 시작노드, 거리 0으로 시작
    q.append((start,0))
    visited = [False] * (N+1)
    # 시작 노드 방문 확인
    visited[start] = True
    while q:
        now, d = q.popleft()
        # 현재 확인하는 노드가 마지막 노드랑 일치하면 거리 리턴
        if now == end:
            return d
        else:
            # now노드에 연관된 노드에 대한 노드번호i와 길이l
            for i, l in graph[now]:
                if not visited[i]:
                    visited[i] = True
                    q.append((i,d+l))
    

for _ in range(N-1):
    n1, n2, l = map(int,input().split())
    graph[n1].append((n2,l))
    graph[n2].append((n1,l))

for _ in range(M):
    n1, n2 = map(int,input().split())
    print(bfs(n1,n2))