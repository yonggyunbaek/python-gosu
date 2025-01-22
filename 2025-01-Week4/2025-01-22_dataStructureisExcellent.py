# https://www.acmicpc.net/problem/23253

import sys

input = sys.stdin.readline

n, m = map(int,input().split())
dummy = []

for _ in range(m):
    k = int(input())
    ks = list(map(int,input().split()))
    for i in range(len(ks)-1):
        if ks[i] < ks[i+1]:
            print('No')
            sys.exit(0)

print('Yes')
