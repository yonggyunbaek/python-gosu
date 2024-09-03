# https://www.acmicpc.net/problem/2776

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    a = set(map(int,input().split()))
    M = int(input())
    b = list(map(int,input().split()))

    for i in b:
        if i in a:
            print(1)
        else:
            print(0)