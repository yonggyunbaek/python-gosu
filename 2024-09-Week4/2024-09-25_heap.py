# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    # 답, 현재시간, 작업횟수
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]]) # 작업소요시간을 앞에 두고 heappush
        if heap: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap) # 작업소요시간 제일 짧은 것 부터
            start = now # 작업 start시간 갱신
            now += cur[0] # 현재시간 갱신 (작업소요시간(cur[0]) 더하기)
            answer += now - cur[1] # 작업 요청시간(cur[1]) 부터 종료시간(now)까지의 시간 계산
            i += 1 # 힙에서 나와서 처리했으므로 작업 횟수 += 1 , else로 가면 작업횟수 증가 안함
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))