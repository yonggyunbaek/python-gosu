# https://www.acmicpc.net/problem/17952

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
score,num=deque(),deque()
for _ in range(n):
    task=list(map(int,input().split()))
    if task[0]==1:
        num.appendleft([task[1],task[2]])
    else:
        pass
    if num:
        num[0][1]-=1
        if num[0][1]==0:
            score.appendleft(num[0][0])
            num.popleft()
    # print(task, score, num)
print(sum(score))
    
    
