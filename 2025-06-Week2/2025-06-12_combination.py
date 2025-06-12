# https://www.acmicpc.net/problem/2407

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a, b = 1, 1
for i in range(m, 0, -1):
    a *= i

for j in range(n, n-m, -1):
    b *= j

print(b // a)