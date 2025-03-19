# https://www.acmicpc.net/problem/16958

from collections import defaultdict
import sys

input = sys.stdin.readline

def distance(a,b):
    return abs(cities[a][0] - cities[b][0]) + abs(cities[a][1] - cities[b][1])

n, t = map(int,input().split())
cities = defaultdict(list)
for i in range(n):
    s, x, y = map(int,input().split())
    cities[i+1].extend([x,y,s])

# print(cities)

m = int(input())
for _ in range(m):
    a, b = map(int,input().split())
    # 두 도시 모두 텔포 안될경우
    if cities[a][2] == 0 and cities[b][2] == 0:
        print(distance(a,b))
        continue
    # 시작점만 텔포 가능하면
    elif cities[a][2] == 1 and cities[b][2] == 0:
        # 도착점에서 가장 가까운 텔포 가능 도시 찾아
        possible = {}
        for i in range(1,n+1):
            if i not in [a,b]:
                if cities[i][2] == 1:
                    possible[distance(b, i)] = i
        mid_city = possible[min(possible.keys())]
        print(min([(distance(a,b)), t+distance(b,mid_city)]))
        continue
    # 도착점만 텔포 가능하면
    elif cities[a][2] == 0 and cities[b][2] == 1:
        # 도착점에서 가장 가까운 텔포 가능 도시 찾아
        possible = {}
        for i in range(1,n+1):
            if i not in [a,b]:
                if cities[i][2] == 1:
                    possible[distance(a, i)] = i
        mid_city = possible[min(possible.keys())]
        print(min([distance(a,b), t+distance(a,mid_city)]))
        continue
    # 시작 도착 둘다 텔포 가능이면
    else:
        print(min(distance(a,b), t))
                    

