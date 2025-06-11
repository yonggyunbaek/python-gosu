# https://www.acmicpc.net/problem/1057

import sys

input = sys.stdin.readline

def nextround(number):
    if number %2 == 0:
        number //= 2
    else:
        number += 1
        number //= 2
    return number

n, kim, im = map(int,input().split())

cnt = 1

while True:
    if kim - im == 1 and kim % 2 == 0:
        break
    elif im - kim == 1 and im % 2 == 0:
        break
    kim = nextround(kim)
    im = nextround(im)
    # print(kim,im)
    cnt += 1

print(cnt)
