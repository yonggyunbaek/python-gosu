# https://www.acmicpc.net/problem/17413

import sys

data = input()

stack = []
ans = ''
check = False # 괄호 여부를 체크
for d in data:
    # 스택에 존재하는 값을 역으로 추가. 첫번째 '<'가 아닐 경우 > 부터 < 사이 문자열 역으로 ans 추가
    if d == '<':
        check = True
        for _ in range(len(stack)):
            ans += stack.pop()

    stack.append(d)

    # 스택에 존재하는 값은 괄호안의 값이기에 순차적으로 추가. < 부터 > 까지 ans에 추가
    if d == '>':
        check = False
        for _ in range(len(stack)):
            ans += stack.pop(0)


    # 스택에 존재하는 값을 역으로 추가. 괄호 밖 상태에서 공백이전까지 값들 역으로 ans에 추가
    if d == ' ' and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            ans += stack.pop()
        ans += ' '

# 스택에 값이 남아있는 경우(괄호 끝나고 추가된 값들 존재)는 괄호의 경우가 아니기에 역으로 추가.
if stack:
    for _ in range(len(stack)):
        ans += stack.pop()

print(ans)