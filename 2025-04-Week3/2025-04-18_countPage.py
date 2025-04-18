# https://www.acmicpc.net/problem/4821

import sys

input = sys.stdin.readline

while True:
    total = int(input())
    page = set()
    if total == 0:
        break
    testcase = input().rstrip()
    tclist = testcase.split(",")
    
    for i in tclist:
        if "-" in i:
            low, high = map(int, i.split('-'))
            if high > total:
                high = total
            if low < 1:
                low = 1

            if low > high:
                continue
            elif low == high:
                page.add(low)
            else:
                for j in range(low, high+1):
                    page.add(j)
        else:
            if int(i) > total or int(i) < 1:
                continue
            page.add(int(i))

    print(len(page))
