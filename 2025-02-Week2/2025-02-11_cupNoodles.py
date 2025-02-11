# https://www.acmicpc.net/problem/1781

import heapq
import sys
input = sys.stdin.readline

n = int(input())
dc = []
for _ in range(n):
    dead, cup = map(int,input().split())
    dc.append((dead, cup))

# 데드라인 빠른것부터 처리, 보상값은 큰것부터
dc.sort(key=lambda x: (x[0], -x[1]))
time, result = 1, 0
hq = []

for d, c in dc:
    # 현재시간보다 deadline이 더 크거나 같으면 (deadline안지났으면)
    if time <= d:
        # 결과값에 보상값 추가
        result += c
        heapq.heappush(hq, (c, time))
        time += 1
    # deadline 지났으면 
    else:
        if hq:
            # (7,1)
            min_tmp = heapq.heappop(hq)
            # hq에 있던 보상값과 새로 들어온 보상값 비교
            if min_tmp[0] < c:
                result += (c - min_tmp[0])
                heapq.heappush(hq, (c, min_tmp[1]))
            # hq에 있던 값이 크면 다시 원래대로 heappush
            else:
                heapq.heappush(hq, min_tmp)
    print(hq, result)
print(result)
