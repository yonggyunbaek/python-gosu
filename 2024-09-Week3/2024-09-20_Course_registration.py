# https://www.acmicpc.net/problem/13414

import sys
input = sys.stdin.readline

k, l = map(int,input().split())

students = dict()
for i in range(l):
    # 학번 int로 받으면 안됨 01234567이 1234567 됨
    student = input().rstrip()
    students[student] = i

s_list = sorted(students.items(), key = lambda x: x[1])[:k]
# print(s_list)
print( *(x[0] for x in s_list), sep='\n')