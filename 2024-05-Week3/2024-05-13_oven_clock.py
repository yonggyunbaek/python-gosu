# https://www.acmicpc.net/problem/2525

import sys
input = sys.stdin.readline

hour, min = map(int,input().split())
need = int(input())

h = need // 60
m = need % 60

hour += h
min += m
    
print((hour + min // 60) % 24 , end = " ")
print(min % 60)