# https://www.acmicpc.net/problem/9996

import sys
import re
input = sys.stdin.readline

n = int(input())
f, b = input().rstrip().split("*")
lf = len(f)
lb = len(b)


for _ in range(n):
    word = input().rstrip()
    if len(word) < lf+lb:
        print('NE')
    else:
        if word[:lf] == f and word[-lb:] == b:
            print('DA')
        else:
            print('NE')
