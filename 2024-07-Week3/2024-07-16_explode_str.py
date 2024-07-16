# https://www.acmicpc.net/problem/9935

import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()

# 시간 초과
# 문자열 길이가 n이고 매 반복마다 문자열이 반으로 줄어든다고 가정하면 O(n*logn)
# 최악의 경우 O(n^2)
# while bumb in string:
#     str_list = list(string.split(bomb))
#     print(str_list)
#     string = "".join(str_list)
#     print(string)

stack = []
bomb_last = bomb[-1]
print(bomb_last)
bomb_len = len(bomb)

for char in string:
    stack.append(char)
    # print(stack)
    if char == bomb_last and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

# 스택 사용하면 문자열 순회 1번 
# 문자열 결합 1번
# O(n)
result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")