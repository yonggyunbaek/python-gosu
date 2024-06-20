# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
    word = input().strip()
    l = len(word)
    words.add((l,word))

for a,b in sorted(words):
    print(b)