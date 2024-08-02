# https://www.acmicpc.net/problem/11502
# 5보다 큰 임의의 홀수는 정확히 세 개의 소수들의 합으로 나타낼 수 있다.

import sys
input = sys.stdin.readline

def prime(x):
    prime = [True] * (x+1) # 체크리스트
    for i in range(2,x+1):
        if prime[i]:
            for j in  range(i*2, x+1, i): # 소수의 배수 확인
                prime[j] = False
    numbers = []
    for i in range(2, x+1):
        if prime[i]:
            numbers.append(i)
    return numbers

def three_prime(numbers, K):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i+j+k == K:
                    return(i,j,k)
    return 0

numbers = prime(1000)

T = int(input())
for _ in range(T):
    K = int(input())
    print(*three_prime(numbers, K))