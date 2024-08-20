# https://www.acmicpc.net/problem/1786
# KMP 알고리즘

import sys
input = sys.stdin.readline

def make_pi():
    pi = [0 for i in range(0, len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if (P[i] == P[j]):
            j += 1
            pi[i] = j
    return pi


def solution(pi):
    result = []
    count = 0

    j = 0
    for i in range(0, len(T)):

        while j > 0 and T[i] != P[j]:
            j = pi[j - 1]

        if T[i] == P[j]:
            if j == (len(P) - 1):
                result.append(i - len(P) + 2)
                count += 1
                j = pi[j]
            else:
                j += 1
            
            print(i,j,count,result)

    print(count)
    print(*result)


T = input().rstrip()
P = input().rstrip()
solution(make_pi())