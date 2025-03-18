# https://www.acmicpc.net/problem/15723

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def dfs(graph:dict, start_node):
    # 방문이 필요한 노드 q
    q = deque()
    visited = []
    # 시작노드 방문해야지
    q.append(start_node)

    # 방문이 필요한 노드가 있으면
    while q:
        node = q.pop()
        # print(node)
        if node not in visited:
            visited.append(node)
            # 인접 노드들 방문 필요한 q에 추가
            # print(graph)
            if graph.get(node):
                q.append(graph.get(node))

    return visited


n = int(input())
premises = defaultdict(str)
for _ in range(n):
    premise = input().split()
    x, y = premise[0], premise[2]
    premises[x] = y

m = int(input())
for _ in range(m):
    conclusion = input().split()
    k, v = conclusion[0], conclusion[2]
    if v in dfs(premises, k):
        print("T")
    else:
        print("F")