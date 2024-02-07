# 나무 2개 심기
# n개의 위치 중 서로 다른 두 곳에 꼭 심어야함
# 1 ~ n 각 위치마다 비옥함 Fi 주어짐
# 위치 a,b 일때 Fa * Fb 최대가 되도록 

import sys
from itertools import combinations

n = sys.stdin.readline()
F_lst = list(map(int, sys.stdin.readline().split())) 

ans_lst = []
for i in list(combinations(F_lst,2)):
    ans_lst.append(i[0]*i[1])

print(max(ans_lst))

