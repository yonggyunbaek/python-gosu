# https://www.acmicpc.net/problem/1009

import sys
input = sys.stdin.readline

t = int(input())

td = { 1:1, 2:4, 3:4, 4:2, 5:1, 6:1, 7:4, 8:4, 9:2, 0:1}

for _ in range(t):
    a, b = map(int,input().split())
    a %= 10
    if td[a] == 1:
        if a== 0:
            print(10)
        else:
            print(a)
    else:
        if b % td[a] != 0:
            b %= td[a]
            answer = (a**b) % 10
            if answer == 0:
                print(10)
            else:
                print(answer)
        else:
            answer = (a**b) % 10
            if answer == 0:
                print(10)
            else:
                print(answer)            