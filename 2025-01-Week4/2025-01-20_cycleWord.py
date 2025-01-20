from collections import deque
import sys

input = sys.stdin.readline

def isword(wordq:deque, check:list):
    if not check:
        # check가 비었으면 추가
        check.append(wordq)
    else:
        for i in range(len(wordq)):
            wordq.rotate(1)  # 단어를 회전시킴
            if wordq in check:
                return check  # 중복된 경우 check를 그대로 반환
        check.append(wordq)  # 중복이 없으면 추가
    return check  # check를 반환

n = int(input())
check = []

for _ in range(n):
    word = input().rstrip()
    wordq = deque(word)
    check = isword(wordq, check)
    # print(check)

print(len(check))
