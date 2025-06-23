
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
piece = 1000
package = 1000
for _ in range(m):
    pa, pi = map(int,input().split())
    piece = min(pi, piece)
    package = min(package, pa)

case = n // 6 + 1
mincost = float("inf")
for i in range(case, -1, -1):
    if (n - i*6) >= 0:
        cost = (n - i*6)*piece + i*package
    else:
        cost = i*package
    mincost = min(mincost, cost)

print(mincost)