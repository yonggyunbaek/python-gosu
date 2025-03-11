# https://www.acmicpc.net/problem/11403

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def dfs(graph, start_node, n):
    visited = defaultdict(int)
    # 방문이 필요한 노드 q
    q = deque()

    # 시작노드 방문해야지
    q.append(start_node)

    # 방문이 필요한 노드가 있으면
    while q:
        node = q.pop()
        if visited[node] < 2:
            # 방문했으니까 visited 추가
            visited[node] += 1
            # 인접 노드들 방문 필요한 q에 추가
            for i in range(n):
                # 인접노드 확인 and 방문 2번까지 확인
                if graph[node][i] == 1 and visited[node] < 2:
                    q.append(i)

    return visited

n = int(input())
graph = [ list(map(int,input().split())) for i in range(n) ]

for i in range(n):
    visitedDict = dfs(graph,i,n)
    # print(visitedDict)
    for j in range(n):
        if visitedDict[j] != 0:
            if i == j and visitedDict[j] == 1:
                print(0, end=" ")
                continue
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()



