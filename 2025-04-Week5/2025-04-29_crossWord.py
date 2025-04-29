# https://www.acmicpc.net/problem/1706

import sys
input = sys.stdin.readline

r, c = map(int,input().split())

tmp = [[] for _ in range(c)]
words = []
for _ in range(r):
    word = input().rstrip()
    for i in range(c):
        tmp[i].append(word[i])
    for w in word.split("#"):
        if len(w) > 1:
            words.append(w)

for c in tmp:
    for w in "".join(c).split("#"):
        if len(w) > 1:
            words.append(w)

print(sorted(words)[0])