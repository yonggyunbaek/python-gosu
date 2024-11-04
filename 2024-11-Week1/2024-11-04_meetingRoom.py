# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())

meetings = [ list(map(int,input().split())) for i in range(n) ]

# 끝나는 시간으로 정렬 (빨리 끝나야 다음 회의 진행해서 회의를 많이한다)
# 끝나는 시간이 같으면 시작시간으로 정렬
meetings.sort(key = lambda x: (x[1], x[0]))

end = 0
answer = 0
for nextStart, nextEnd in meetings:
    if end <= nextStart:
        answer += 1
        end = nextEnd

print(answer)