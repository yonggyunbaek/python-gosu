# 연비측정
# 3대 의 연비 9, 15, 20 일 경우 중앙값은 15
# n대 중에 q개의 질의에 대해 3대를 골라 중앙값 mi 나오는 서로 다른 경우의 수를 구하는 프로그램

# 5 3
# 5 2 3 1 6
# 1
# 3
# 6

# n q
# 연비 n개
# m1
# m2
# m3

import sys

n, q = map(int, sys.stdin.readline().split())
fe_list = list(map(int, sys.stdin.readline().split()))
fe_list.sort()


answer_dict = {}
for i in fe_list:
    answer_dict[i] = fe_list.index(i) * (len(fe_list) - fe_list.index(i) - 1)

# print(answer_dict)
for _ in range(q):
    m = int(input())
    answer = answer_dict.get(m, 0)
    print(answer)