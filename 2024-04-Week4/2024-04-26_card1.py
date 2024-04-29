import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque( i for i in range(1,N+1))

while len(q) > 1:
    print(q.popleft(), end= " ")
    q.append(q.popleft())

print(q[0])