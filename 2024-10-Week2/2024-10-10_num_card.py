# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
m = int(input())
test = list(map(int,input().split()))

num_dict = {}
for i in num:
    if num_dict.get(i):
        num_dict[i] += 1
    else:
        num_dict[i] = 1

for i in test:
    print(num_dict.get(i) if num_dict.get(i) else 0, end=' ')
