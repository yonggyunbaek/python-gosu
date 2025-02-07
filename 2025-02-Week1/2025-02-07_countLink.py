# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

# 정점의 개수 N과 간선의 개수 M
n, m = map(int, input().split())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [ i for i in range(n+1) ]

for i in range(m):
    u, v = map(int,input().split())
    union(u,v)

answer = set()
for i in range(1,n+1):
    answer.add(find(i))

print(len(answer))

