# https://www.acmicpc.net/problem/1958

import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

def LCS(x:str, y:str, z:str):
    x = [0] + list(x)
    y = [0] + list(y)
    z = [0] + list(z)
    lx = len(x)
    ly = len(y)
    lz = len(z)
    LCSstr = []
    LCSGraph = [[ [0]*lz for _ in range(ly) ] for _ in range(lx)]
    for i in range(1,lx):
        for j in range(1,ly):
            for k in range(1,lz):
                if x[i] == y[j] == z[k]:
                    LCSGraph[i][j][k] = LCSGraph[i-1][j-1][k-1] + 1
                    LCSstr.append(x[i])
                else:
                    LCSGraph[i][j][k] = max(LCSGraph[i-1][j][k], LCSGraph[i][j-1][k], LCSGraph[i][j][k-1])
    
    return LCSGraph[-1][-1][-1]

print(LCS(a,b,c))

