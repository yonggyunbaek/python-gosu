# https://www.acmicpc.net/problem/15828

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
packets = deque()
while True:
    p = int(input())
    if p == -1:
        break
    elif p == 0:
        packets.popleft()
    else:
        if len(packets) < n:
            packets.append(p)
        else:
            continue
if not packets:
    print("empty")
else:          
    print(*packets)