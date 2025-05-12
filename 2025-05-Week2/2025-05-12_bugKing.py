# https://www.acmicpc.net/problem/3447

import sys
# readlines -> ctrl+d 로 끊음

for i in sys.stdin.readlines():
    while True:
        if "BUG" in i:
            # replace는 새로운 문자열을 반환
            i = i.replace("BUG","")
        else:
            break
    print(i,end="")

# print("여러 줄을 입력하세요. 끝내려면 EOF (Ctrl+D / Ctrl+Z):")
# lines = sys.stdin.readlines()
# print("입력된 줄 리스트:", lines)