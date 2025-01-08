# https://www.acmicpc.net/problem/4307

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, n = map(int, input().split())
    ant = [ int(input()) for i in range(n) ]
    # print(ant)
    minl = max([ i if i <= l//2 else l-i for i in ant ])
    maxl = max([ l-i if i <= l//2 else i for i in ant ])
    print(minl, maxl)