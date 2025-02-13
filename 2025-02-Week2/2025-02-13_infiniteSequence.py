# https://www.acmicpc.net/problem/1351

import sys
input = sys.stdin.readline

n, p, q = map(int,input().split())

# 시간 초과
# def A(i:int):
#     if i == 0:
#         return 1
#     return A(int(i/p)) + A(int(i/q))

# print(A(n))

# 메모이제이션 구현 위한 딕셔너리
cache = {}

def A(i:int):
    if i == 0:
        return 1
    # cache 확인
    if i in cache:
        return cache[i]
    result = A(int(i/p)) + A(int(i/q))
    cache[i] = result
    return result

print(A(n))