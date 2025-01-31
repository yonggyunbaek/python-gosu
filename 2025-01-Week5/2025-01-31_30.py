# https://www.acmicpc.net/problem/13116

import sys, math
input = sys.stdin.readline

# 런타임에러
# def getTreePath(a: int) -> set:
#     path = set()
#     while a != 1:
#         a = a // 2
#         path.add(a)
#     path.add(1)
#     return path

# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     print(max(getTreePath(a) & getTreePath(b))*10)


def getLevel(a:int) -> int:
    return math.floor(math.log2(a))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    while True:
        la, lb = getLevel(a), getLevel(b)
        if la > lb:
            a //= 2
        elif la < lb:
            b //= 2
        else:
            break
    while a != b:
        a //= 2
        b //= 2
    print( a * 10)