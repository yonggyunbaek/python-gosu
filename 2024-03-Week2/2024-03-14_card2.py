# https://www.acmicpc.net/problem/2164

import sys
from collections import deque
N = int(sys.stdin.readline().strip())

card = deque(range(1,N+1))

while len(card) != 1:
    card.popleft()
    if len(card) == 1:
        break
    card.append(card.popleft())

print(card[0])
