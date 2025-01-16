# https://www.acmicpc.net/problem/5670

from collections import defaultdict
import sys
input = sys.stdin.readline

def strToMin(time:str):
    h,m = map(int,time.split(":"))
    return h*60 + m

timelst = [ strToMin(i) for i in input().split() ]
startCheck = set()
endCheck = set()

while True:
    try:
        t, name = input().split()
    except:
        break
    tm = strToMin(t)
    if tm <= timelst[0]:
        startCheck.add(name)
    elif timelst[1] <= tm <= timelst[2]:
        endCheck.add(name)

print(len( startCheck&endCheck))


