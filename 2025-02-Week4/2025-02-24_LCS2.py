# https://www.acmicpc.net/problem/9252

import sys
input = sys.stdin.readline

def LCS(stra,strb):
    a = [""] + list(stra)
    b = [""] + list(strb)
    la = len(a)
    lb = len(b)
    g = [ [""]*lb for _ in range(la) ]
    for i in range(1,la):
        for j in range(1,lb):
            if a[i] == b[j]:
                g[i][j] = g[i-1][j-1] + a[i]
            else:
                if len(g[i-1][j]) >= len(g[i][j-1]):
                    g[i][j] = g[i-1][j]
                else:
                    g[i][j] = g[i][j-1]
    return g[-1][-1]



stra = input().rstrip()
strb = input().rstrip()
result = LCS(stra,strb)
print(len(result), result, sep="\n")