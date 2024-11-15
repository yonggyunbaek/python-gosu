# https://www.acmicpc.net/problem/1969

import sys
from collections import Counter
n, m = map(int, input().split())

dnas = [ list(input().rstrip()) for _ in range(n) ]
cnt = 0
answerDna = ''
for i in range(m):
    x = Counter([dna[i] for dna in dnas])
    x = sorted(x.items(), key=lambda item:(-item[1], item[0]))
    l = len(x)
    if len(x) != 1:
        for j in range(1,l):
            cnt += x[j][1]
    answerDna += x[0][0]

print(answerDna)
print(cnt)

