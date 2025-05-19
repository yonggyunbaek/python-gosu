# https://www.acmicpc.net/problem/5376

from math import gcd
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    i, d = input().rstrip().split(".")
    if '(' in d:
        ft, repeat = d.split("(")
        repeat = repeat[:-1]
        # 분모
        denominator = 10**(len(ft)) * (10**len(repeat)-1)
        if ft == '':
            numerator = int(repeat)
        else:
            numerator = int(ft+repeat) - int(ft)
    else:
        denominator = 10 ** len(d)
        numerator = int(d)

    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor

    print(f"{numerator}/{denominator}")


