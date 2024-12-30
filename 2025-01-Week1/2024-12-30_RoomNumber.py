# https://www.acmicpc.net/problem/1475

import sys
input = sys.stdin.readline

n = list(map(int,input().rstrip()))
counter = {}

for i in n:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)

if 9 in counter:
    if 6 in counter:
        counter[6] += counter[9]
        counter[9] = 0
    else:
        counter[6] = counter[9]
        counter[9] = 0

print(counter)
if 6 in counter:
    if counter[6] % 2 == 0:
        counter[6] //= 2 
    else:
        counter[6] //= 2 
        counter[6] += 1
print(counter)
print(max([ v for k,v in counter.items() ]))

