# https://www.acmicpc.net/problem/13904

import sys
import heapq
input = sys.stdin.readline

N = int(input())
day_score = []
daylst=[]
for _ in range(N):
    day, score = map(int,input().split())
    daylst.append(day)
    heapq.heappush(day_score, [-score, day])
answer = [0] * (max(daylst))
while day_score:
    values = heapq.heappop(day_score)
    score = - values[0]
    day = values[1]
    # print(score,day)
    if answer[day] == 0:
        answer[day] = score
    elif day > 1:
        for i in range(day-1,0,-1):
            # print(i)
            if answer[i] == 0:
                answer[i] = score
                break
    # print(answer)
print(sum(answer))

