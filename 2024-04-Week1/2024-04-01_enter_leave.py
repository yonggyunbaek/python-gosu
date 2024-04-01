# https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline

N = int(input())

company = set()
for _ in range(N):
    name, io = input().split()
    if io == "enter":
        company.add(name)
    else:
        company.remove(name)

for i in sorted(company, reverse=True):
    print(i)


# list의 remove는 항상 O(len)
# set은 해시맵을 이용해서 조회에 필요한 시간복잡도가 O(1)