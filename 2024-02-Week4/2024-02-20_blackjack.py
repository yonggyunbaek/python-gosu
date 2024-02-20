# 백준 2798

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))


combi = list(combinations(num_list, 3))
sum_list = []
for i in range(len(combi)):
    v = sum(combi[i])
    if v <=  M:
        sum_list.append(v)

print(max(sum_list))
        
    

