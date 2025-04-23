# https://www.acmicpc.net/problem/15725

from collections import deque
import sys

input = sys.stdin.readline

e = list(input().rstrip())
sign = '+'
tmp = []

for i in e:
    if i.isdigit():
        tmp.append(i)
    elif i == '-':
        sign = '-'
        tmp = []
    elif i == '+':
        tmp = []
    else:
        if not tmp:
            answer = 1
        else:
            answer = int(''.join(tmp))
        if sign == '-':
            answer *= -1
        print(answer)
        break

else:
    print(0)


