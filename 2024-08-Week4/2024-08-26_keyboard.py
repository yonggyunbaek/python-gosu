# https://school.programmers.co.kr/learn/courses/30/lessons/160586?language=python3
def solution(keymap, targets):
    answer = []
    
    for target in targets:
        total_presses = 0
        
        for char in target:
            min_presses = float('inf')
            for key in keymap:
                if char in key:
                    min_presses = min(min_presses, key.index(char) + 1)
            if min_presses == float('inf'):
                total_presses = -1
                break
            total_presses += min_presses
            
        answer.append(total_presses)
    
    return answer
