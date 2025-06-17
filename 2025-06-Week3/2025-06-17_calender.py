# https://www.acmicpc.net/problem/6064

import sys

input = sys.stdin.readline

# 최소공약수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

# 최대공약수
def lcm(a, b):
    return m * n / gcd(a, b)

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    max_year = lcm(m , n)
    answer = x
    while answer <= max_year: 
        if (answer - 1)%n + 1 == y:
            break
        answer += m
    if answer > max_year:
        print(-1)
    else:
        print(answer)