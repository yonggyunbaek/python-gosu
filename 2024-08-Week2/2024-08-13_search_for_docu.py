# https://www.acmicpc.net/problem/1543

import sys
from collections import deque
input = sys.stdin.readline

docu = input().rstrip()
word = input().rstrip()

i = 0
cnt = 0

while i < len(docu):
    if docu[i:i+len(word)] == word:
        cnt += 1
        i += len(word)
    else:
        i += 1
print(cnt)
