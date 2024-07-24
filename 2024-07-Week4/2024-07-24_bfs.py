#https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    # BFS를 위한 큐 초기화
    queue = deque([(x, 0)])  # (현재 값, 연산 횟수)
    visited = set()
    visited.add(x)

    while queue:
        current, steps = queue.popleft()
        if current == y:
            return steps
        # 1. x + n
        next_add = current + n
        if next_add <= y and next_add not in visited:
            visited.add(next_add)
            queue.append((next_add, steps + 1))
        
        # 2. x * 2
        next_mul2 = current * 2
        if next_mul2 <= y and next_mul2 not in visited:
            visited.add(next_mul2)
            queue.append((next_mul2, steps + 1))
        
        # 3. x * 3
        next_mul3 = current * 3
        if next_mul3 <= y and next_mul3 not in visited:
            visited.add(next_mul3)
            queue.append((next_mul3, steps + 1))

    # y에 도달할 수 없는 경우
    return -1