# https://www.acmicpc.net/problem/27649

import sys
input = sys.stdin.readline

cmd = input().rstrip()

delimiters = ['<', '>', '(', ')', " "]
idx = 0
tmp = []
for i in range(len(cmd)):
    if cmd[i] in delimiters:
        tmp.append(cmd[idx:i])
        tmp.append(cmd[i])
        idx = i+1
    elif cmd[i] == '|' and i < len(cmd)-1 and i >= idx:
        if cmd[i+1] =='|':
            tmp.append(cmd[idx:i])
            tmp.append(cmd[i:i+2])
            idx = i+2
    elif cmd[i] == '&' and i < len(cmd)-1 and i >= idx:
        if cmd[i+1] =='&':
            tmp.append(cmd[idx:i])
            tmp.append(cmd[i:i+2])
            idx = i+2
    elif cmd[i] == ' ':
        tmp.append(cmd[idx:i])
        idx = i+1
tmp.append(cmd[idx:])

for i in tmp:
    if i == '' or i == ' ':
        continue
    else:
        print(i, end=' ')