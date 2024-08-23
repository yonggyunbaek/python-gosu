# https://www.acmicpc.net/problem/1652

import sys
input = sys.stdin.readline

n = int(input())
room = [ input().rstrip() for _ in range(n) ]
l_cnt = 0
w_cnt = 0
for i in range(n):
    for a in room[i].split("X"):
        if ".." in a:
            l_cnt += 1
    for b in ''.join([ room[j][i] for j in range(n) ]).split("X"):
        if ".." in b:
            w_cnt += 1

print(l_cnt, w_cnt)
