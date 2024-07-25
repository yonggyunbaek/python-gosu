# https://softeer.ai/practice/9657

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n) ]

for _ in range(2):
    a, b = map(int,input().split())
    for i in range(a-1,b):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0
                print(i,j,grid)
                break
            else:
                continue

print(sum(sum(grid,[])))
