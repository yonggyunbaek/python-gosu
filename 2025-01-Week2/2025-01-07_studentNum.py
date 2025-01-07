# https://www.acmicpc.net/problem/1235

import sys
input = sys.stdin.readline

n = int(input())
sn = [ input().rstrip() for i in range(n) ]

l = -1
while True:
    test = set([ i[l:] for i in sn ])
    if len(test) == n:
        print(l*-1)
        break
    l -= 1

