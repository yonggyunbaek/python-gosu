# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    count = 0
    while s:
        x = s[0]
        x_count = 0  # x의 개수
        none_count = 0  # x가 아닌 글자의 개수
        
        for char in s:
            if char == x:
                x_count += 1
            else:
                none_count += 1
            
            # 두 개수가 같아지는 순간
            if x_count == none_count:
                count += 1
                s = s[x_count + none_count:]
                break
        else:
            count += 1
            break
    
    return count
