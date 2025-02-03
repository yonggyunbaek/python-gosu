# https://www.acmicpc.net/problem/17352

import sys
input = sys.stdin.readline


# 찾기 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find_parent(x):
    # 루트 노드가 아니라면, 루트노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 합집합 연산(두 집합을 합치기 위한 함수)
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: # 값이 더 작은 쪽을 부모로
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

parent = [i for i in range(n + 1)] # 자기 자신을 부모로 갖는 n + 1개 집합

for _ in range(n-2):
    a, b = map(int, input().split())
    union_parent(a,b)
    print(parent)

for i in range(2,n+1):
    if find_parent(1) != find_parent(i):
        print(1,i)
        break