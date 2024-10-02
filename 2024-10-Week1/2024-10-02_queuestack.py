# https://www.acmicpc.net/problem/24511

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))

queuestack = deque()
for i in range(n):
    if a[i] == 0:
        queuestack.append(b[i])
print(queuestack)

for i in c:
    queuestack.appendleft(i)
    ans = queuestack.pop()
    print(ans,end=" ")

    
