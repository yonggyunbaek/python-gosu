# https://www.acmicpc.net/problem/16562

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if friend_cost[a] < friend_cost[b]:
            parent[b] = a
        else:
            parent[a] = b

N, M, k = map(int, input().split())
friend_cost = [0] + list(map(int, input().split()))
parent = list(range(N + 1))

for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

total_cost = 0
visited = set()

for i in range(1, N + 1):
    root = find(i)
    if root not in visited:
        visited.add(root)
        total_cost += friend_cost[root]

if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")