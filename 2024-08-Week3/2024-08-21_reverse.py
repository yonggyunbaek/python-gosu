# https://www.acmicpc.net/problem/1439

import sys
input = sys.stdin.readline

S = input().rstrip()

a = S.split('0')
b = S.split('1')

a_cnt = len(a) - a.count('')
b_cnt = len(b) - b.count('')

print(min(a_cnt, b_cnt))
