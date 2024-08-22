# https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin.readline

name_dict = {}
cnt = 0
while True:

    name = input().rstrip()
    if not name:
        break
    if name in name_dict:
        name_dict[name] += 1
    else:
        name_dict[name] = 1
    cnt += 1


for k, v in sorted(name_dict.items()):
    print("%s %.4f" % (k, v*100/cnt))

# round는 소수점 끝이 0이면 출력 x
# both round(0.5) and round(-0.5) are 0, and round(1.5) is 2