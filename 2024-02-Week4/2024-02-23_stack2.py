# 백준  28278

import sys
input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    x = list(map(int, input().split()))
    
    if x[0] == 1:
        stack.append(x[1])
    elif x[0]== 2:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif x[0] == 3:
        print(len(stack))
    
    elif x[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 5:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)