"""
https://softeer.ai/app/assessment/index.html?xid=103112&xsrfToken=9G5VgT0SWgZR6v4RpFvZQjgkEWBF2xS1&testType=practice
"""

import sys

house_num = sys.stdin.readline()
house_arr = sorted(map(int,sys.stdin.readline().split()))

# print(house_arr)
ans = 0
for n in range(2, house_arr[-1]+1):
    coal = 0

    for h in house_arr:
        if h % n == 0:
            coal += 1

    ans = max(ans, coal)

print(ans)