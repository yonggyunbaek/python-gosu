# https://www.acmicpc.net/problem/28702

import sys

input = sys.stdin.readline

s = [ input().rstrip() for _ in range(3) ]

for i in range(3):
    if s[i].isdigit():
        v = int(s[i]) + (3-i)
        break

if v % 3 == 0 and v % 5 == 0:
    print("FizzBuzz")
elif v % 3 == 0 and v % 5 != 0:
    print("Fizz")
elif v % 3 != 0 and v % 5 == 0:
    print("Buzz")
else:
    print(v)
