# 백준 2563

import sys
input = sys.stdin.readline

n = int(input())

def coloring(paper, x,y,x2,y2):
    for i in range(x, x2):
        for j in range(y, y2):
            paper[i][j] = 1
    return paper

paper = [ [0] * 100 for _ in range(100) ]

xylist = [list(map(int, input().split())) for _ in range(n)]

for x,y in xylist :
    x2 = x + 10
    y2 = y + 10
    coloring(paper,x,y,x2,y2)

print(sum(sum(paper,[])))