# https://www.acmicpc.net/problem/2740

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = [ list(map(int,input().split())) for _ in range(n) ]
m, k = map(int,input().split())
b = [ list(map(int,input().split())) for _ in range(m) ]
pivotb=[]
for i in range(k):
    tmp = []
    for j in range(m):
        tmp.append(b[j][i])
    pivotb.append(tmp)
# print(b, pivotb)

for i in a:
    answer = []
    for j in pivotb:
        answer.append(sum(x * y for x, y in zip(i, j)))
    print(*answer)

