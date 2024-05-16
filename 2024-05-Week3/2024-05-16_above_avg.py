# https://www.acmicpc.net/problem/4344

import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    score = list(map(int,input().split()))
    N = score[0]
    avg = sum(score[1:]) // N
    cnt = 0
    for i in score[1:]:
        if i > avg:
            cnt += 1

    num = cnt / N * 100
    print(f'{num:.3f}', end='')
    print('%') 
