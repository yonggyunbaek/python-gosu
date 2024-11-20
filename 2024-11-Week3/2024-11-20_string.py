# https://www.acmicpc.net/problem/1120

import sys
input = sys.stdin.readline

def sol(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

a,b = input().split()
A = len(a)
B = len(b)
if A == B:
    answer = sol(a,b)
# elif a in b:
#     answer = 0
else:
    answerlist = []
    for i in range(B-A+1):
        # print(a,b[i:i+A])
        answerlist.append(sol(a,b[i:i+A]))
        # print(answerlist)
    answer = min(answerlist)

print(answer)