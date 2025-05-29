# https://www.acmicpc.net/problem/1629

import sys

input = sys.stdin.readline

A,B,C = map(int,input().split())

# 나머지 연산 (AxB)%C = (A%C)*(B%C) % C

# B가 홀수면
# (A**B)%C = ((A**B//2)%C * (A**B//2)%C * A) %C
# B가 짝수면
# (A**B)%C = ((A**B//2)%C * (A**B//2)%C) %C
# 재귀로 반복해서 B 가 1이 되면 A%C리턴(tmp)하고 재귀 빠져나오면서 (tmp*tmp) % C  이런식으로 tmp 갱신하고 첫 mod_op빠져나오면 그게 답

# A의 n승을 C로 나눈 나머지 구하기
def mod_op(A, n):
    if n == 1:
        return A % C
    else:
        tmp = mod_op(A, n//2)
        if n % 2 == 0:
            return(tmp * tmp) % C
        else:
            return(tmp * tmp * A) % C

print(mod_op(A,B))