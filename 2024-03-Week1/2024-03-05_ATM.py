# 백준 11399

import sys
input = sys.stdin.readline

N = int(input())
t_lst = list(map(int,input().split()))

t_lst.sort()

answer = 0
for i in range(N):
    answer += sum(t_lst[:i+1])

print(answer)