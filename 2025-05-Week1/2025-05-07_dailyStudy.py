# https://www.acmicpc.net/problem/29730

import re
import sys
input = sys.stdin.readline

n = int(input())
tmp = []
last = []

for _ in range(n):
    study = input().rstrip()
    s =  re.fullmatch("boj\.kr\/(\d+)", study)
    if s:
        if 1 <= int(s.group(1)) <= 30000:
            last.append((int(s.group(1)), study))
    else:
        tmp.append((len(study), study))

last.sort(key=lambda x: x[0], reverse=False)
tmp.sort(key=lambda x: (x[0], x))

for _, x in tmp:
    print(x)
for _, y in last:
    print(y)