# https://www.acmicpc.net/problem/1357

import sys
input = sys.stdin.readline

a, b = input().split()

def reverse(s):
    rs = s[::-1]
    return rs

print( int(reverse(str(int(reverse(a)) + int(reverse(b))))) )
