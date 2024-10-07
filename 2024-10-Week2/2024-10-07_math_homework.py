# https://www.acmicpc.net/problem/2870

import sys
import re
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range(n):
    s = input().rstrip()
    answer += list(map(int,re.findall(r'\d+', s)))

print(*(sorted(answer)), sep='\n')
