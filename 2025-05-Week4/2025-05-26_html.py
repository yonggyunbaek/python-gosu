# https://www.acmicpc.net/problem/6581

import re
import sys
input = sys.stdin.readlines

lines = []
for i in input():
    i = i.strip()
    lines.extend(re.sub(r'\s+', ' ', i).split())

tmp =''

for l in lines:
    if l == "<br>":
        print(tmp.rstrip())
        tmp = ''
    elif l == "<hr>":
        if tmp:
            print(tmp.rstrip())
            tmp = ''
        print('-'*80)
    else:
        if tmp == '':
            tmp = l
        elif len(tmp) + 1 + len(l) <= 80:
            tmp += ' ' + l
        else:
            print(tmp)
            tmp = l
if len(tmp) != 0:
    print(tmp.rstrip())
    


