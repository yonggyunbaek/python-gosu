# https://www.acmicpc.net/problem/21942

from collections import defaultdict
from datetime import datetime, timedelta
import sys

input = sys.stdin.readline

# 개수, 대여기간, 벌금
n, l, f = input().split()

d, h = l.split("/")
d = int(d)
hh, mm = map(int,h.split(":"))

minute = d*24*60 + hh*60 + mm

records = {}
idmin = []
for i in range(int(n)):
    dt, tm, parts, id = input().split()
    strtodate = datetime.strptime(dt+' '+tm, '%Y-%m-%d %H:%M')
    paid = parts+' '+id
    if records.get(paid):
        idmin.append((paid,-(records[paid] - strtodate).total_seconds() / 60))
        del records[paid]
    else:
        records[paid] = strtodate

# print(records, idmin)

answerdict = defaultdict(int)
flag = False
for id, min in idmin:
    if min > minute:
        answerdict[id.split()[1]] += int(int(f)*(min-minute))

if not answerdict:
    print(-1)
else:
    for key in sorted(answerdict):
        print(f"{key} {answerdict[key]}")

