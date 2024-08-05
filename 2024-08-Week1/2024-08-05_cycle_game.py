# https://www.acmicpc.net/problem/20040

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


# n개의 점 (0 ~ n-1)
# m번 게임 진행
n,m = map(int,input().split())

# 각요소가 각자의 집합 대표하는 상태로 초기화 
parent = [ i for i in range(n) ]

for i in range(m):
    a, b = map(int,input().split())
    if find_parent(a) == find_parent(b):
        print(i+1)
        break
    union_parent(a,b)

# for 문이 break안걸리고 끝나면
else:
    print(0)

