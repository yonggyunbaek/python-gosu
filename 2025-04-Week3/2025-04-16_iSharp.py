# https://www.acmicpc.net/problem/3568
import sys
input = sys.stdin.readline

l = input().rstrip()[:-1].replace(",","").split()
# print(l)
for i in range(1,len(l)):
    rev = ''
    alpha = ''
    for j in l[i]:
        if j.isalpha():
            alpha += j
        elif j == "*" or j == "&":
            rev += j
        elif j == "[":
            rev +=']'
        elif j == "]":
            rev +="["
    print(l[0] + rev[::-1], alpha+";")