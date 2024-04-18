# https://www.acmicpc.net/problem/2504

arr=input()
stack=[]

answer=0
tmp=1
for i in range(len(arr)):
    # 열린 괄호는 스택에 넣고 tmp에 숫자 곱
    if arr[i] =='(':
        stack.append(arr[i])
        tmp *=2
    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *=3
    
    # 닫힌 괄호는 
    elif arr[i] == ")":
        # 쌍인지 확인하고 스택이 비어있거나 짝이 안맞으면 답 0으로 끝
        if not stack or stack[-1] == "[":
            answer = 0 # 실패
            break
        # 쌍이 맞으면 현재 tmp값 answer더해주고 stack에서 맞는 쌍 pop
        if arr[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2  #tmp 1로 초기화
    else:
        if not stack or stack[-1] == "(":
            answer=0
            break
        if arr[i-1] =='[':
            answer+=tmp
        stack.pop()
        tmp //=3 #tmp 1로 초기화
    # print(stack, tmp, answer)

if stack:
    print(0)
else:
    print(answer)