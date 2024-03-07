# 백준 2751

import sys
input = sys.stdin.readline

N = int(input())
data = []

for i in range(N):
    age, name = input().split()
    data.append((i,int(age),name))

data.sort(key=lambda x : (x[1], x[0]))

for i in range(N):
    print(data[i][1], data[i][2])