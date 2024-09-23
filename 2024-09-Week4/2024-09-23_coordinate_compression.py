# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))

sc = sorted(set(c))
dictc = { sc[i]:i for i in range(len(sc)) }


for i in c:
    print(dictc[i], end=" ")
