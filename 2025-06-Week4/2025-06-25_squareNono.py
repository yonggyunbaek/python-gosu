# https://www.acmicpc.net/problem/1016

import sys
import math
input = sys.stdin.readline

mi, ma = map(int,input().split())


length = ma - mi + 1
checked = [False] * length  # 마킹 배열

for i in range(2, int(math.sqrt(ma)) + 1):
    square = i * i
    start = ((mi + square - 1) // square) * square  # mi 이상이면서 square의 배수인 시작점
    for j in range(start, ma + 1, square):
        checked[j - mi] = True

print(checked.count(False))


# 소수 제곱수의 배수 제외 -> 시간초과
# def is_primenum(x):
#     for i in range (2, int(math.sqrt(x)) + 1):
#     	if x % i == 0:
#             return False
#     return True

# ex = set()
# for i in range(mi, ma+1):
#     if i == 1:
#         continue
#     if is_primenum(i):
#         v = 1
#         while ((i**(2)) * v) <= ma:
#             # print(i, (i**(2)) * v)
#             ex.add((i**(2)) * v)
#             v += 1

# print(ma - mi + 1 - len(ex))