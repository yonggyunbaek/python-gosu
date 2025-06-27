# https://www.acmicpc.net/problem/2485

import sys

from math import gcd
input = sys.stdin.readline

n = int(input())
trees = []
forgcd = []

for _ in range(n):
    tree = int(input())
    if not trees:
        trees.append(tree)
        continue
    else:
        forgcd.append(tree-trees[-1])
        trees.append(tree)
        
    
g = forgcd[0]
for i in range(1,len(forgcd)):
    g = gcd(g,forgcd[i])

distance = trees[-1] - trees[0]
treecnt = distance//g + 1
print(treecnt - len(trees))