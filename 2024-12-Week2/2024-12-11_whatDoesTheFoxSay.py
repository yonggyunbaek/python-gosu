import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

notfox = []

for _ in range(n):
    sound = input().split()
    while True:
        case = input().rstrip()
        if case == "what does the fox say?":
            break
        else:
            clist = case.split()
            print(clist)
            notfox.append(clist[2])
            
    for i in sound:
        if i in notfox:
            continue
        else:
            print(i, end=" ")
    print("")
