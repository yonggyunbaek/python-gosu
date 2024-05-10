# https://www.acmicpc.net/problem/25304

import sys

input = sys.stdin.readline

X = int(input())
N = int(input())

answer = 0
for _ in range(N):
    cost, cnt = map(int, input().split())
    answer += (cost*cnt)

if X == answer:
    print('Yes')
else:
    print('No')