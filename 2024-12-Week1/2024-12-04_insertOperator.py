# https://www.acmicpc.net/problem/14888

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))
ops = list(map(int,input().split()))
op = '+'*ops[0] + '-'*ops[1] + '*'*ops[2] + '/'*ops[3]
op_perm = permutations(op, n-1)
# [('+', '*'), ('*', '+')]

max_result = - int(1e9)
min_result = int(1e9)

for p in op_perm:
    result = number[0]
    for i in range(1,n):
        if p[i-1] == '+':
            result += number[i]
        elif p[i-1] == '-':
            result -= number[i]
        elif p[i-1] == '*':
            result *= number[i]
        elif p[i-1] == '/':
            if result < 0 and number[i] > 0: 
                result = -1*( result*(-1) // number[i])
            else:
                result //= number[i]          
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)

# 음수를 양수로 나눠 몫을 구할 때는 양수로 바꿨다가 계산 후 다시 음수로 
# >>> print(-9//2)
# -5
# >>> print(9//2)
# 4