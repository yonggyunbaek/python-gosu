# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter
def solution(N, stages):
    answer = []
    stages_count = Counter(stages) # 도전자 수 (분자)
    stages_cleared = {s : 0 for s in range(1,N+1)}
    
    total_user = len(stages)
    for num in range(1,N+1):
        if stages_count[num] == 0:
            continue
        
        stages_cleared[num] = stages_count[num] / total_user
        total_user -= stages_count[num]
    
    # print(stages_cleared)
    answer = sorted(stages_cleared,key=lambda x: stages_cleared[x], reverse=True)
    return answer
