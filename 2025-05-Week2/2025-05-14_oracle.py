# https://www.acmicpc.net/problem/7656

import sys
import re

input = sys.stdin.readline

question = re.findall(r'\bWhat\b[^.]*?\?', input().rstrip())
print(question)
for q in question:
    print(q.replace('What','Forty-two').replace("?","."))


        
