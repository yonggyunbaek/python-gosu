from collections import defaultdict
import sys

input = sys.stdin.readline

def distance(c1,c2):
    return abs(cities[c1][0] - cities[c2][0]) + abs(cities[c1][1] - cities[c2][1])

def findCloseTeleDistance(city):
    min_d = 10000
    for i in range(1,n+1):
        if i != city:
            if cities[i][2] == 1:
                min_d = min(min_d,distance(city, i))
    return min_d   

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
    # 그냥 거리계산, 텔포가능한 도시 중간에 2개 껴서 가기 중 짧은 것
    if cities[a][2] == 0 and cities[b][2] == 0:
        print(min(distance(a,b), findCloseTeleDistance(a)+t+findCloseTeleDistance(b)))
        continue
    # 시작점만 텔포 가능하면
    elif cities[a][2] == 1 and cities[b][2] == 0:
        # 도착점에서 가장 가까운 텔포 가능 도시 찾아
        print(min(findCloseTeleDistance(b)+t,distance(a,b)))
        continue
    # 도착점만 텔포 가능하면
    elif cities[a][2] == 0 and cities[b][2] == 1:
        # 시작점에서 가장 가까운 텔포 가능 도시 찾아
        print(min(findCloseTeleDistance(a)+t,distance(a,b)))
        continue
    # 시작 도착 둘다 텔포 가능이면
    else:
        print(min(distance(a,b), t))
                    