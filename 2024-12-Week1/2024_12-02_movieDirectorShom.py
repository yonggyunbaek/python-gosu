# https://www.acmicpc.net/problem/1436

import sys
input = sys.stdin.readline

n = int(input())
start = 666
cnt = 0
while cnt < 10001:
    if '666' in str(start):
        cnt += 1
        if cnt == n:
            print(start)
            break
    start += 1
