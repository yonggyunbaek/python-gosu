# https://www.acmicpc.net/problem/12605

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    s = input().rstrip().split(" ")
    print(f"Case #{i+1}:", *s[::-1])

