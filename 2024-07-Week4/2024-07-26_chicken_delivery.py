# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

# 그래프 순회 하면서 집, 치킨 좌표 저장
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])


for chi in combinations(chick, m):  # chi는 m개의 치킨집 (m개 좌표)
    temp = 0            # 도시의 치킨 거리
    for h in house: # 집 좌표 하나씩
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m): # 집에서 m개 치킨집 중에 제일 가까운 거 찾기
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    # combi(chi는 m개의 치킨집) 순회하면서 최소 치킨거리 갱신
    result = min(result, temp)

print(result)