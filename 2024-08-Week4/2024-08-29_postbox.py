# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque

def solution(order):
    answer = 0
    queue = deque(order)
    tmp_queue = deque()

    for i in range(1, len(order) + 1):
        tmp_queue.append(i)  # 현재 아이템을 임시 큐에 추가

        # 임시 큐의 마지막이 큐의 첫 번째와 같으면, 큐에서 제거
        while tmp_queue and tmp_queue[-1] == queue[0]:
            tmp_queue.pop()
            queue.popleft()
            answer += 1

    return answer
