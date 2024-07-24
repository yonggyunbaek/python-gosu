# https://www.acmicpc.net/problem/10610
# 모든 자리수의 합이 3의 배수이면 그 숫자는 3의 배수

import sys
input = sys.stdin.readline

N = input().rstrip()

if '0' not in N:
    print(-1)

else:
    n_sum = 0
    for i in range(len(N)):
        n_sum += int(N[i])

    if n_sum % 3 != 0:
        print(-1)
    else:
        answer = ''.join(sorted(N, reverse=True))
        print(answer)

    

