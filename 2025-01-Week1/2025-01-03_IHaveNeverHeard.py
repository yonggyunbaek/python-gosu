# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nh = set(input().rstrip() for _ in range(n))
ns = set(input().rstrip() for _ in range(m))

answer = nh&ns
print(len(answer))
for i in sorted(answer):
    print(i)