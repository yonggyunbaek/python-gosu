# https://www.acmicpc.net/problem/26069

import sys
input = sys.stdin.readline

n = int(input())
dance = {'ChongChong'}

for _ in range(n):
    a, b = input().split()
    
    if a in dance:
        dance.add(b)
    elif b in dance:
        dance.add(a)

print(len(dance))