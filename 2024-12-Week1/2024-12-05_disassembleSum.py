# https://www.acmicpc.net/problem/2231

import sys
input = sys.stdin.readline


def main(n):
    if n == 1:
        return(0)
    else:
        for i in range(1,n):
            sum_n = 0
            for j in str(i):
                sum_n += int(j)
            if i + sum_n == n:
                return(i)
    return(0)

n = int(input())
print(main(n))