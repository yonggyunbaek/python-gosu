# https://www.acmicpc.net/problem/11725

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

visited = [0] * (N+1)

def dfs(node):
    for i in graph[node]: # 대상노드에 인접 노드 중
        if visited[i] == 0: # 방문한 적 없는 노드면
            visited[i] = node # 대상노드를 인접노드의 부모노드로 저장
            
            print(i,node,visited)
            dfs(i)
print("i,node,visited")
dfs(1)

for i in range(2,N+1):
    print(visited[i])