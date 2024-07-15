#https://school.programmers.co.kr/learn/courses/30/lessons/92341


from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    # 입차 시간 기록
    in_time = defaultdict()
    # 누적 시간
    cum_time = defaultdict()
    
    default_time, default_fee, sep_time, sep_fee = fees
    for r in records:
        cur_time, car_num, record = r.split()
        parsed_time = int(cur_time.split(":")[0])*60 + int(cur_time.split(":")[1])
        
        if record == "IN":
            in_time[car_num] = parsed_time
        
        if record == "OUT": # OUT
            cum_time[car_num] = (parsed_time - in_time[car_num]) + cum_time.get(car_num, 0)
            del in_time[car_num]
    
    if in_time:
        for k, v in in_time.items():
            cum_time[k] = (1439 - v) + cum_time.get(k, 0)
    
    for car_num, total_time in sorted(cum_time.items()):
        if total_time <= default_time:
            answer.append(default_fee)
        else:
            answer.append(default_fee + math.ceil((total_time - default_time)/sep_time) * sep_fee)
    
    return answer