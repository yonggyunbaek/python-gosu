# https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

str_a = [0] + list(input().rstrip())
str_b = [0] + list(input().rstrip())

LCS = [ [0]*len(str_a) for i in range(len(str_b)) ] 

for j in range(1,len(str_b)):
    for i in range(1,len(str_a)):
        if str_b[j] == str_a[i]:
            LCS[j][i] = LCS[j-1][i-1] + 1
        else:
            LCS[j][i] = max(LCS[j-1][i], LCS[j][i-1])
        # print(j,i,LCS)

print(LCS[-1][-1])