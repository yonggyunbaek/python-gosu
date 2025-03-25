# https://www.acmicpc.net/problem/1972

import sys
input = sys.stdin.readline

def surprising(word:str):
    n = len(word)
    cnt = 0
    for d in range(n-1):
        temp = set()
        for i in range(n-d-1):
            temp.add(word[i]+word[i+1+d])
        # print(temp)
        if len(temp) == n-d-1:
            cnt += 1
    if cnt == n-1:
        return True
    return False

while True:
    word = input().rstrip()
    if word == "*":
        break
    else:
        if surprising(word):
            print(word, "is surprising.")
        else:
            print(word, "is NOT surprising.")
