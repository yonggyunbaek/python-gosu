# https://www.acmicpc.net/problem/11051

import sys

input = sys.stdin.readline

def factorial(num):
    for i in range(num-1,0,-1):
        num *= i
    return num

n, k = map(int, input().split())

a = factorial(n)
b = factorial(n-k)
c = factorial(k)

print(a//(b*c) % 10007)