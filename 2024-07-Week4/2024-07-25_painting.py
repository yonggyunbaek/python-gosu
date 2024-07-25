# https://school.programmers.co.kr/learn/courses/30/lessons/161989#
from collections import deque
def solution(n, m, section):
    queue = deque(section)
    
    answer = 1
    start_section = queue.popleft() # 2
    paint_range = start_section + m - 1 # 5
    while queue:
        cur_section = queue.popleft() # 3, 6
        
        if cur_section <= paint_range: # 3 <= 5
            continue
        else: # 6 > 5
            paint_range = cur_section + m - 1
            answer += 1
    
    return answer
