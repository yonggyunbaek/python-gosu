# https://www.acmicpc.net/problem/10822

import sys
input = sys.stdin.readline

answer = 0
for s in map(int,input().split(",")):
    answer += s

print(answer)