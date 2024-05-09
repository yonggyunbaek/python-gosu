# https://www.acmicpc.net/problem/10798

import sys

input = sys.stdin.readline

word = [ list(input().strip()) for _ in range(5) ]
word_len = [ len(i) for i in word ]
# print(word, word_len)

for i in range(max(word_len)):
    for j in range(5):
        # print(i,j)
        # print("len", word_len[j],i)
        if word_len[j] > i:
            print(word[j][i],end="")