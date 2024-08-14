# https://www.acmicpc.net/problem/10820

import sys
input = sys.stdin.readline

def analysis(string):
    lower = 0
    upper = 0
    number = 0
    space = 0

    for i in string:
        if i.isalpha():
            if i.islower():
                lower += 1
            else:
                upper += 1
        elif i.isdigit():
            number += 1
        else:
            space += 1

    print(lower, upper, number, space)

while True:
    string = list(input().rstrip("\n"))
    if not string:
        break
    analysis(string)

