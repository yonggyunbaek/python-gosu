# https://www.acmicpc.net/problem/25757

import sys
from collections import deque

input = sys.stdin.readline

ngame = input().split()
n = int(ngame[0])
game = ngame[1]

minNum = { 'Y':2, 'F':3, 'O':4 }

c = minNum[game]
already = set()
party = deque()
answer = 0
for i in range(n):
    name = input().rstrip()
    if name not in already:
        party.append(name)
        if len(party) == c-1:
            answer += 1
            already.update(party)
            party.clear()

print(answer)



# deque의 append, clear 가 set의 add, union보다 빠르다