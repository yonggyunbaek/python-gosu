# https://www.acmicpc.net/problem/11365

import sys
input = sys.stdin.readline

def f(wordList):
    for word in reversed(wordList):
        print(word[::-1], end=" ")

while True:
    wl = input().rstrip().split()
    if wl[0] == "END":
        break    
    f(wl)
    print()

