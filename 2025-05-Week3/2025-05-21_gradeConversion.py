# https://www.acmicpc.net/problem/31799

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
asis = []

tmp = deque()
for i in list(input().rstrip()):
    if i in ["A","B","C"]:
        if tmp:
            asis.append(tmp.popleft()+"0")
        tmp.append(i)
    elif i in ["+", "-", "0"]:
        asis.append(tmp.popleft()+i)

if tmp:
    asis.append(tmp.popleft()+"0")
# print(asis)
tobe = []
for i in range(n):
    if asis[i] in ["C+", "C0", "C-"]:
        tobe.append("B")
    elif asis[i] in ["B0", "B-"]:
        if i == 0 or asis[i-1] in ["C+", "C0", "C-"]:
            tobe.append("D")
        elif asis[i-1] in ["A+", "A0", "A-", "B+", "B0", "B-"]:
            tobe.append("B")
    elif asis[i] in ["A-", "B+"]:
        if i == 0 or asis[i-1] in ["B0", "B-", "C+", "C0", "C-"]:
            tobe.append("P")
        elif asis[i-1] in ["A+", "A0", "A-", "B+"]:
            tobe.append("D")
    elif asis[i] == "A0":
        if i == 0 or asis[i-1] in ["A-", "B+", "B0", "B-", "C+", "C0", "C-"]:
            tobe.append("E")
        elif asis[i-1] in ["A+", "A0"]:
            tobe.append("P")
    elif asis[i] == "A+":
        tobe.append("E")

print(*tobe,sep="")