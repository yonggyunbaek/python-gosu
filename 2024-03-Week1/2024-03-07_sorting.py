# 백준 2750

import sys
input = sys.stdin.readline

N = int(input())
numlst = [ int(input()) for _ in range(N) ]

numlst.sort()

for i in range(N):
    print(numlst[i])