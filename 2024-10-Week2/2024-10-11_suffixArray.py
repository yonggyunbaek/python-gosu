# https://www.acmicpc.net/problem/11656

import sys
input = sys.stdin.readline

s = input().rstrip()
l = len(s)
suffix = [ s[i:] for i in range(l) ]
print(*sorted(suffix), sep="\n")