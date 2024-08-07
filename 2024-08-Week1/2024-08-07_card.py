# https://www.acmicpc.net/problem/11652

import sys

input = sys.stdin.readline
dict = {}

n = int(input())
for _ in range(n):
    a = int(input())
    dict.setdefault(a, 0)
    dict[a] += 1

# 시간 초과
# max계산에서 dict 모든 값 순회 O(n)
# 리스트 컴프리헨션 items 순회 O(n)
# min 에서 O(n)
# 최악의 경우 3n
# vmax_key = [ k for k,v in dict.items() if v == max(dict.values()) ]
# print(min(vmax_key))


# dict.items() O(n)
# sorted() (n log n)
# O(n log n) 이지만 sorted는 최적화가 잘되어있다?
vmax_key = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
print(vmax_key[0][0])
