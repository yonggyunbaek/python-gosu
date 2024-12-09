# https://www.acmicpc.net/problem/9733

from collections import Counter
import sys

input = sys.stdin.readline

works = []
while True:
    work = input().split()
    if len(work) == 0:
        break
    works += work

cnt = len(works)
workDict = Counter(works)

for i in ['Re','Pt','Cc','Ea','Tb','Cm','Ex']:  
    print(i, workDict[i], f'{workDict[i] / cnt:.2f}')

print('Total', cnt, '1.00')