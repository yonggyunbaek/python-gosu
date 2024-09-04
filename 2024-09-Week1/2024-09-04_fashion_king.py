# https://www.acmicpc.net/problem/9375

import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    kind_dict = defaultdict(int)
    answer = 1
    for i in range(n):
        name, kind = input().split()
        kind_dict[kind] += 1 

    for k,v in kind_dict.items():
        answer *= (v+1)

    print(answer - 1)


