# https://www.acmicpc.net/problem/5637

import re
import sys
input = sys.stdin.readline

maxl = 0

while True:
    line = input()
    # 문자열에서 소문자, 대문자, 하이픈 제외한 나머지 제거하고 단어 추출
    words = re.findall(r"[a-zA-Z\-]+", line) 
    # print(words)
    for i in words:
        if maxl < len(i):
            maxl = len(i)
            lw = i
        if i == "E-N-D":
            print(lw.lower())
            sys.exit()


