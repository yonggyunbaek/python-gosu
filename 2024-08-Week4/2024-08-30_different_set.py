# https://www.acmicpc.net/problem/1822

import sys
input = sys.stdin.readline

na, nb = map(int,input().split())

a = set(map(int,input().split()))
b = set(map(int,input().split()))

answer = sorted(a - b)
print(len(answer))
if len(answer) != 0:
    print(*answer)