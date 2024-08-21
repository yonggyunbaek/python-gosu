# https://www.acmicpc.net/problem/3059

import sys
input = sys.stdin.readline

T = int(input())

base = set( i for i in range(65,91) )

for _ in range(T):
    s = input().rstrip()
    s_num = set(map(lambda x:ord(x), list(s)))
    print(sum(base - s_num))

