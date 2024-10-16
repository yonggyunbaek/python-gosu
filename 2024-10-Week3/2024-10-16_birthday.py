# https://www.acmicpc.net/problem/5635

import sys
input = sys.stdin.readline

n = int(input())
birth = []

for _ in range(n):
    name, d, m, y = input().split()
    if len(m) == 1:
        m = '0'+ m
    if len(d) == 1:
        d = '0'+ d
    birth.append((int(y+m+d), name))

birth.sort()
print(birth[-1][1], birth[0][1], sep="\n")


    
