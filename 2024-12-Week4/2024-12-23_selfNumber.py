# https://www.acmicpc.net/problem/4673

import sys
input = sys.stdin.readline

def selfNumber(n:int) -> int:
    if n < 10000:
        return n + sum(list(map(int, str(n))))
answer = [ i for i in range(1,10001) ]

for i in range(1,10001):
    try:
        answer.remove(selfNumber(i))
    except:
        pass

for i in answer:
    print(i)