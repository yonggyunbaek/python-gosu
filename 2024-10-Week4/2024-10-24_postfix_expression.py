# https://www.acmicpc.net/problem/1918

from collections import deque
import sys
input = sys.stdin.readline

infix = list(input().rstrip())
opstack = deque()
answer = ''
priority = { '+':1,
             '-':1,
             '*':2,
             '/':2,
             '(':3,
             ')':3 }
for i in infix:
    if i not in priority:
        answer += i
    elif i == '(':
        opstack.append(i)
    # ) 나오면 스택에서 ( 나올 때까지 pop
    elif i == ')':
        while opstack[-1] != "(":
            answer += opstack.pop()
        # '(' 제거
        opstack.pop()
    elif i in priority:
        while opstack and opstack[-1] != "("  and priority[opstack[-1]] >= priority[i]:
            answer += opstack.pop()
        opstack.append(i)
    # print(answer, opstack)

while opstack:
    answer += opstack.pop()

print(answer)
