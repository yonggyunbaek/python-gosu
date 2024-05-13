# https://www.acmicpc.net/problem/2525

import sys
input = sys.stdin.readline

hour, min = map(int,input().split())
need = int(input())

h = need // 60
m = need % 60

hour += h
min += m

if min >= 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour -= 24
    
print(hour, end = " ")
print(min)