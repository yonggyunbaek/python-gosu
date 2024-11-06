# https://www.acmicpc.net/problem/9933

import sys
input = sys.stdin.readline

n = int(input())
words = [ input().strip() for _ in range(n) ]

for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word)//2])
        break

