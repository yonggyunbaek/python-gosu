# https://www.acmicpc.net/problem/1340

from datetime import datetime
import sys
input = sys.stdin.readline

d = input().split()


month = datetime.strptime(d[0], "%B").month
day = int(d[1][:-1])
year = int(d[2])
hour, min = d[3].split(":")
h = int(hour)
m = int(min)


start = datetime(year, 1, 1, 0, 0)
end = datetime(year, month, day, h, m)
secondToNextYear = datetime(year+1, 1, 1, 0, 0)

print((end-start).total_seconds()/(secondToNextYear-start).total_seconds()*100)