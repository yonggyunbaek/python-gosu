# https://www.acmicpc.net/problem/1907

import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

def strToDict(c:str):
    cntdict = defaultdict(int)
    for i in range(len(c)):
        if c[i] in ['C','H','O']:
            cntdict[c[i]] += 1
        else:
            cntdict[c[i-1]] += 1*(int(c[i])-1)
    return cntdict

def coefficient(cc:list):
    ans = []
    a = strToDict(cc[0])
    b = strToDict(cc[1])
    c = strToDict(cc[2])
    for i in range(1,11):
        for j in range(1,11):
            for k in range(1,11):
                if a['C']*i + b['C']*j == c['C']*k and \
                   a['H']*i + b['H']*j == c['H']*k and \
                   a['O']*i + b['O']*j == c['O']*k:
                    ans.append([i,j,k])
    return ans

cc = input().replace("+", " ").replace("=", " ").split()
print(*coefficient(cc)[0])