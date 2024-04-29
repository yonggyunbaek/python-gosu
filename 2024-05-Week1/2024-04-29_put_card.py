# https://www.acmicpc.net/problem/5568

import sys
import itertools
input = sys.stdin.readline

n = int(input())
k = int(input())
card = list( input().strip() for i in range(n))

nPr = itertools.permutations(card,k)
numset = set()
for i in list(nPr):
    numset.add(''.join(i))
    # print(numset)

print(len(numset))