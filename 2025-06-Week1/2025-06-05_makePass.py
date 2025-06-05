# https://www.acmicpc.net/problem/1759

from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int,input().split())
alpha = input().split()
consonant, vowel = [], []

for i in alpha:
    if i in ['a','e','i','o','u']:
        vowel.append(i)
    else:
        consonant.append(i)

answer = set()
for i in range(1,l-1):
    combi_v = list(combinations(vowel, i))
    combi_c = list(combinations(consonant, l - i))
    # print(combi_c, combi_v)
    for j in combi_v:
        for k in combi_c:
            answer.add(''.join(sorted(j+k)))

print(*sorted(answer), sep='\n')
