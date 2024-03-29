# https://www.acmicpc.net/problem/1302

import sys
input = sys.stdin.readline

N = int(input())

dict = {}
for _ in range(N):
    book = input().strip()

    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1

answer = [ k for k,v in dict.items() if max(dict.values()) == v ]
answer.sort()
print(answer[0])