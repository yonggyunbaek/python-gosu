# https://www.acmicpc.net/board/search/all/problem/1918/37729

strn = list(input())
stack=[]
ans=''
for s in strn:
    # 알파벳이면 ans에 추가
    if s.isalpha():
        ans+=s
    # 알파벳 아니면
    else:
        # 괄호 확인
        # "("이면 스택에 추가
        if s == '(':
            stack.append(s)
        # *, /면
        elif s == '*' or s == '/':
            # 스택에 있는 모든 *, / ans에 추가
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                ans += stack.pop()
            stack.append(s)
        # +,-이면 stack에 있던 모든연산자 pop해서 ans에 추가하고 스택에 +,- 추가
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                ans+= stack.pop()
            stack.append(s)
        # ")" 이면 stack.pop()을 "("전까지 하고 "("는 pop해서 제거
        elif s == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
    print("ans", ans)
    print("stack", stack)

# 남아있는 스택 전부 ans에 붙이기
while stack :
    ans+=stack.pop()
print(ans)
