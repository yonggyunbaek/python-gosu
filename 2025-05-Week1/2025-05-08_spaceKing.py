# https://www.acmicpc.net/problem/3518

from collections import defaultdict
import sys
input = sys.stdin.readline

ls = []
idxMaxL = defaultdict(int)

while True:
    l = input().strip().split()
    if not l:
        break
    for i in range(len(l)):
        if idxMaxL[i] < len(l[i]):
            idxMaxL[i] = len(l[i])
    ls.append(l)

# print(ls)
# print(idxMaxL)

for wordlst in ls:
    answer = ''
    for i in range(len(wordlst)):
        # print(word,end=' ')
        answer += wordlst[i]+' '*(idxMaxL[i] - len(wordlst[i]))
        answer += ' '
    print(answer.rstrip())