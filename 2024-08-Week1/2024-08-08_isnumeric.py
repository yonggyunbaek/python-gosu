# https://school.programmers.co.kr/learn/courses/30/lessons/81301

from collections import deque
def solution(s):
    num_dict = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    queue = deque(s)
    answer = ''
    
    while queue:
        cur_num = ''
        while True:
            x = queue.popleft()
            if x.isnumeric():
                cur_num += x 
                break
                
            cur_num += x
            if cur_num in num_dict:
                cur_num = num_dict[cur_num]
                break
            else:
                continue
            
        answer += cur_num
    # print(answer)
    return int(answer)
