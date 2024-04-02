# https://www.acmicpc.net/problem/10799

import sys
p = sys.stdin.readline().strip()
print(p)
stack = []
count = 0

for i in range(len(p)):
    print(stack)
    if p[i] == "(":
        stack.append(p[i])

    # p[i]는 ")" 
    else:
        # 바로 앞에가 "(" 이면 -> 레이저
        if p[i-1] == "(":
            stack.pop()
            count += len(stack)
        
        # 레이저 아닌 ")" 나오면
        else:
            # 짝 맞춰졌으니 pop
            stack.pop()
            # 막대기 끝
            count += 1

print(count)