# https://www.acmicpc.net/problem/4949

import sys
input = sys.stdin.readline

def balance(sentence):
    stack = []
    for i in sentence:

        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                # 스택이 비어있을 경우 균형 안맞는 거 append 하고 break 하면 stack에 값 있으니까 answer는 no
                stack.append(i)
                break            
    
    if len(stack) == 0 :
        answer = "yes"
    else:
        answer = "no"
    return answer


while True:
    sentence = input().rstrip()
    if sentence == ".":
        break
    
    answer = balance(sentence)
    print(answer)