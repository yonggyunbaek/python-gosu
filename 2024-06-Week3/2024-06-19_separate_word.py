# https://www.acmicpc.net/problem/1251

import sys
input = sys.stdin.readline

word = list(input().strip())
answer = []

for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        first = ''.join(reversed(word[:i]))
        second = ''.join(reversed(word[i:j]))
        third = ''.join(reversed(word[j:]))
        answer.append(first+second+third)

print(min(answer))