# https://www.acmicpc.net/problem/18258

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
answer = deque()
for _ in range(N):
    A = list(input().split())
    if len(A) > 1:
        cmd = A[0]
        v = A[1]
        if cmd == "push":
            answer.append(v)
        
    else:
        cmd = A[0]
        if cmd == "pop":
            if answer:
                print(answer.popleft())
            else:
                print(-1)

        elif cmd == "size":
            print(len(answer))

        elif cmd == "empty":
            if len(answer) == 0:
                print(1)
            else:
                print(0)

        elif cmd == "front":
            if len(answer) != 0:
                print(answer[0])
            else:
                print(-1)

        elif cmd == "back":
            if len(answer) != 0:
                print(answer[-1])
            else:
                print(-1)

    