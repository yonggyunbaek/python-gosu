# https://www.acmicpc.net/problem/1789

s = int(input())
answer = 0
for i in range(1,4294967295):
    if i*(i+1) > 2*s:
        answer = i-1
        break
    elif i*(i+1) == 2*s:
        answer = i
        break
print(answer)