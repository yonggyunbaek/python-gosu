# https://www.acmicpc.net/problem/11000

import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = []

for _ in range(N):
    time.append(list(map(int,input().split(' '))))
# 시작시간으로 정렬
time.sort(key=lambda x : x[0])

# 정렬 후 첫번째 강의 끝나는 시간 time[0][1]
heap = [time[0][1]]
# print(heap)

# 두 번째 부터 마지막 강의 까지 확인
for i in range(1,N):
    # 현재 heap에 들어있는 끝나는 시간보다 다음번 강의의 시작 시간이 크거나 같으면 (강의가 안겹치면 = 강의실 한 개로 이어서 사용 가능)
    if heap[0] <= time[i][0]:
        # heap에 있던 가장 작은 끝나는 시간 pop
        heapq.heappop(heap)
    # 다음번 강의 끝나는 시간 push
    heapq.heappush(heap,time[i][1])
    # print(heap)

print(len(heap))
