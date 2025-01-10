# https://www.acmicpc.net/problem/9613

from itertools import combinations
import sys
input = sys.stdin.readline

def gcd(a,b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for _ in range(t):
    answer = 0
    nums = sorted(list(map(int, input().split()))[1:])
    combi = list(combinations(nums,2))
    for a,b in combi:
        answer += gcd(a,b)
    print(answer)