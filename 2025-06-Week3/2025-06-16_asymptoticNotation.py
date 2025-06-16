# https://www.acmicpc.net/problem/24313

import sys
input = sys.stdin.readline

a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

# a1, c는 각 일차함수 기울기로 생각
# x = n0일때 확인 그리고 기울기가 같거나 커야함
if a1*n0 + a0 <= c*n0 and a1 <= c:
    print(1)
else:
    print(0)

