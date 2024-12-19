# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations, permutations
input = sys.stdin.readline


def ability(team:tuple) -> int:
    v = 0
    for i,j in permutations(team, 2):
        v += (s[i][j])
    return v


n = int(input())
s = [[0]*(n+1)] + [ [0] + list(map(int, input().split())) for _ in range(n) ]
# print(n, s)

teams = list(combinations(range(1,n+1),n//2))
l = len(teams)

answer = sys.maxsize
for i in range(l//2):
    # print(teams[i], teams[l-i-1])
    now = abs(ability(teams[i]) - ability(teams[l-i-1]))
    if now < answer:
        answer = now

print(answer)