# https://www.acmicpc.net/problem/12787/

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    m, n = input().split()
    if m == '1':
        tolist = list(map(int,n.split(".")))
        tostr = '0b'
        for j in tolist:
            b = format(j, 'b')
            b = "0"*(8-len(b)) + str(b)
            tostr += b
        print(int(tostr, 2))
    
    else:
        tobin = format(int(n),'b')
        tobin = "0"*(64-len(tobin)) + str(tobin)
        toipv8 = []
        for j in range(0,64,8):
            tempbin = tobin[j:j+8]
            toipv8.append( int('0b'+tempbin, 2) )
        print(*toipv8, sep=".")