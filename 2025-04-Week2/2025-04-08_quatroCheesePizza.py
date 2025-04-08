# https://www.acmicpc.net/problem/27964

import sys

input = sys.stdin.readline

n = int(input())
cheese = input().split()

quattro = set()
for i in cheese:
    if "Cheese" in i and i[-6:] == "Cheese":
        quattro.add(i)

if len(quattro) >= 4:
    print("yummy")
else:
    print("sad")
