# https://www.acmicpc.net/problem/10775

# UNION FIND
# 처음에는 각 요소는 각자의 집합을 대표한다. [0,1,2,3,4] 
# 0,1 두요소를 union한다고 하면 1의 대표가 0으로 바뀐다. [0,0,2,3,4]

import sys

input = sys.stdin.readline

# x라는 요소에대해 x가 속해져 있는 대표 원소를 반환
def find_parent(x):
    # x라는 인덱스(자식)와 인덱스에 대한 값(부모)이 같아야 리턴 -> 다르면 같을 때 까지 재귀
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 각 요소의 집합을 합친다
def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
plane = []
for _ in range(P):
    plane.append(int(input()))

count = 0
for p in plane:
    x = find_parent(p)
    # 부모노드 0이면 이후 비행기 모두 도킹 안됨
    if x == 0:
        break
    # 부모 0아니면 이전
    union_parent(x, x-1)
    # union 횟수 출력
    count += 1

print(count)
    