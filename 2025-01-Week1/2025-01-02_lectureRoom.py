# https://www.acmicpc.net/problem/1374

# from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

# 메모리 초과
# lecture = [ list(map(int,input().split())) for i in range(n) ]
# lcounter = {}

# for a, x, y in lecture:
#     for i in range(x+1,y+1):
#         lcounter.setdefault(i,0)
#         lcounter[i] += 1

# print(max( [ v for k, v in lcounter.items()] ))


# 시작시간으로 정렬 후 끝나는 시간으로 heapq 생성하고 시작시간이 끝나는 시간 따라잡으면 heappop , 과정마다 cnt는 max갱신

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
# 시작시간 정렬
l.sort(key=lambda x: x[1])

# 끝나는 시간 
room = []
cnt = 0
# 시작시간 순서대로 순회
for i in l:
    # 가장 일찍 끝나는 시간보다 시작 시간이 크면
    while room and room[0] <= i[1]:
        # 끝나는 시간 리스트에서 가장 빨리 끝나는 시간 pop
        heapq.heappop(room)
    # 끝나는 시간 추가
    heapq.heappush(room, i[2])
    # print(i, room)
    cnt = max(cnt, len(room))


print(cnt)