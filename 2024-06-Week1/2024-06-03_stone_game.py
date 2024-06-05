# https://www.acmicpc.net/problem/9656

import sys
input = sys.stdin.readline

N = int(input())

if N % 2 == 1:
    ans = 'CY'
else:
    ans = 'SK'

print(ans)