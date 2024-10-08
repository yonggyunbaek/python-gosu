# https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations

input = sys.stdin.readline

height = [ int(input()) for _ in range(9) ]

def find(height):
    for c in combinations(height, 7):
        if sum(c) == 100:
            return sorted(c)
        
print( *find(height), sep="\n")