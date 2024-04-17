# https://www.acmicpc.net/problem/20291

import sys

input = sys.stdin.readline
N = int(input())
dict = {}
for _ in range(N):
    s = input().strip().split(".")[-1]
    if not s in dict:
        dict[s] = 1
    else:
        dict[s] += 1

for key, value in sorted(dict.items()):
    print(key, value)