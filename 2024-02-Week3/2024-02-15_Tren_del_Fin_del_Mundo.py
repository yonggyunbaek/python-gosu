import sys

input = sys.stdin.readline

N = int(input())
station = [ list(map(int,input().split())) for _ in range(N) ]

station.sort(key=lambda x:x[1])
print(" ".join(map(str, station[0])))

