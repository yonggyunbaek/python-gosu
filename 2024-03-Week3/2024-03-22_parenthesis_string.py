# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    s=input()
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else: # ) 차례에 스택 비어있으면 
                print("NO")
                break
    else: # break 안되고 넘어와서
        if not stack: # 스택이 비어있다면 짝 맞음
            print("YES")
        else: # 스택에 괄호가 남아 있으면
            print("NO")