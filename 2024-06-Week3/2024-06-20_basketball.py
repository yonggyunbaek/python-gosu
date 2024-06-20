# https://www.acmicpc.net/problem/1159


import sys
input = sys.stdin.readline

N = int(input())
answer = dict()
for _ in range(N):
    name = input().rstrip()
    last = name[0]

    if last in answer:
        answer[last] += 1
    else:
        answer[last] = 1


s =''
for k, v in sorted(answer.items()):
    print(k,v)
    if v >= 5:
        s += k

if len(s) == 0:
    print("PREDAJA")
else:
    print(s)
