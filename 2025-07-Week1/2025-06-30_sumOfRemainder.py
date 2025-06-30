# https://www.acmicpc.net/problem/10986


import sys, math
input = sys.stdin.readline

n, m = map(int,input().split())
a = [0] + list(map(int,input().split()))

for i in range(1, n+1):
    a[i] += a[i-1]
    a[i] %= m

remainder_counts = [0] * m
for remainder in a:
    remainder_counts[remainder] += 1
    
answer = 0
for i in range(0, m):  
    k = remainder_counts[i]
    answer += math.comb(k,2)

print(answer)
