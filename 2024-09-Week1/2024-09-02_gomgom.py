# https://www.acmicpc.net/problem/25192

import sys
input = sys.stdin.readline

N = int(input())
gomlist = set()
cnt = 0
for _ in range(N):
    chat = input().rstrip()
    if chat == "ENTER":
        gomlist = set()
    else:
        if chat not in gomlist:
            gomlist.add(chat)
            cnt += 1

print(cnt)
