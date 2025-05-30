# https://www.acmicpc.net/problem/6603

from itertools import combinations
import sys

input = sys.stdin.readline

while True:
    testCase = list(map(int,input().split()))
    if testCase == [0]:
        break
    k = testCase[0]
    for i in list(combinations(testCase[1:],6)):
        print(*i)
    print()