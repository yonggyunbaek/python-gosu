import sys
input = sys.stdin.readline

n = int(input())

lhs = [0 for _ in range(1001)]
for _ in range(n):
    l, h = map(int, input().split())
    lhs[l] = h
max_idx = lhs.index(max(lhs))

max_val = 0
for i in range(max_idx):
    max_val = max(max_val, lhs[i])
    lhs[i] = max_val

max_val = 0
for i in range(1000, max_idx, -1):
    max_val = max(max_val, lhs[i])
    lhs[i] = max_val

print(sum(lhs))