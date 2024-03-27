# https://www.acmicpc.net/problem/17219

import sys
input = sys.stdin.readline

N,M = map(int, input().split())

dict = {}
for _ in range(N):
    address, passwd = input().split()
    dict[address] = passwd

for _ in range(M):
    print(dict.get(input().strip()))