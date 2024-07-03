# https://www.acmicpc.net/problem/9372

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    for j in range(M):
        a, b = map(int, input().split())
    print(N - 1)


# 모든 정점(나라)을 방문할 수 있는 가장 적은 간선(비행기)의 수를 구한다
# 연결그래프니까 N-1이 답

# 신장 트리 (Spanning Tree)
# 한 그래프의 부분 그래프, 그래프에서 모든 정점을 포함
# 정점 간 서로 연결되어있어야 한다
# 사이클이 존재하지 않는다
