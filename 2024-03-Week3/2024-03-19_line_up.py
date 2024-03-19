# https://www.acmicpc.net/problem/2252

# 위상정렬 - 사이클이 없는 방향 그래프에서 노드 순서 찾기

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [ [] for _ in range(n+1) ]
#진입차수 - 인덱스가 노드 번호
degree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

queue = deque()

# queue에 진입차수 0인 노드 넣고 시작
for i in range(1,n+1):
    if degree[i] == 0:
        queue.append(i)

# queue에 아무것도 없을 때까지
while queue:
    # 진입차수 0인거 pop 
    now = queue.popleft()
    print(now, end=" ")
    
    # now노드에서 향하는 다음 노드들
    for next in graph[now]:
        # 다음 노드들 차수 -1
        degree[next] -= 1
        
        # 차수 0이면 queue에 추가
        if degree[next] == 0:
            queue.append(next)


