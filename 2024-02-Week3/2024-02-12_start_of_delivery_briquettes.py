# 산타 연탄배달
# 도시에 n개마을 , 1차 수직선 상에 위치
# 가장 가까운 두 마을 먼저 방문, 산타가 처음 방문할 가능성이 있는 서로 다른 두 마을 조합의 수를 구하는 프로그램

# 5
# 1 3 5 8 10
# 가장 가까운 거리2인 경우의 수 3출력

import sys

n = int(input())
town_lst = list(map(int, sys.stdin.readline().split()))

t_diff = [ town_lst[i+1] - town_lst[i] for i in range(n-1)]
min_diff = min(t_diff)

print(t_diff.count(min_diff))

# cnt = 0
# for i in t_diff:
#     if i == min_diff:
#         cnt += 1

# print(cnt)