# https://www.acmicpc.net/problem/15829

import sys
input = sys.stdin.readline

L = int(input())
r = 31
M = 1234567891

d = dict()
for i in range(ord('a'), ord('z')+1):
    # print(chr(i))
    d[chr(i)] = i-ord('a')+1

s = input().rstrip()
answer = 0
for i in range(L):
    answer += (d[s[i]] * r**i)
    # print(answer)
    if answer > M:
        answer = answer%M
    else:
        continue

print(answer)
