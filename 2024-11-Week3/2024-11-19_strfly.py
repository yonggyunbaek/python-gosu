# https://www.acmicpc.net/problem/11328

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().split()
    
    if sorted(list(a)) == sorted(list(b)):
        print("Possible")
    else:
        print("Impossible")