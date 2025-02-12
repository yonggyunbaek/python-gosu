# https://www.acmicpc.net/problem/13334

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    # 시작점, 도착점
    h, o = map(int,input().split())
    if h > o:
        data.append([o, h])
    else:
        data.append([h, o])

d = int(input())
# 도착점 오름차순 정렬
data.sort(key=lambda x: (x[1], x[0]))

hq = []
maxv = 0
for i in range(n):
    end = data[i][1]
    start = data[i][0]
    # print("start, end", start,end)
    if end - start <= d:
        # 철로 길이에 해당되면 시작점만 hq에 넣기
        heapq.heappush(hq, start)
    else:
        continue

    # hq에 값이 있으면
    while len(hq) != 0:
        # 가장 왼편의 좌표와
        tmp = hq[0]
        # print('tmp',tmp)
        # 순회 되면서 오는 end값까지의 길이가 철로 길이보다 작은지 확인
        if end-tmp <= d:
            break
        # 길이를 벗어나면 pop
        else:
            heapq.heappop(hq)
    maxv = max(maxv, len(hq))
    # print(hq)
print(maxv)
