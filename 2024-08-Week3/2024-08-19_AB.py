# https://www.acmicpc.net/problem/12904

import sys

input = sys.stdin.readline


def A(word):
    return word[:-1]  # 마지막 'A' 제거

def B(word):
    return word[:-1][::-1]  # 마지막 'B' 제거하고 뒤집기


init_S = input().rstrip()
T = input().rstrip()


# 역방향으로 처리
while len(T) > len(init_S):
    if T[-1] == 'A':
        T = A(T)
    elif T[-1] == 'B':
        T = B(T)

# 최종적으로 init_S와 같다면 성공
if T == init_S:
    print(1)
else:
    print(0)
