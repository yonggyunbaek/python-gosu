# https://www.acmicpc.net/problem/2902

import sys
input = sys.stdin.readline

fullname = input().rstrip()

# answer = [ i[0] for i in fullname.split("-")]
# print(''.join(answer))

print(''.join(map(lambda x:x [0], fullname.split("-"))))