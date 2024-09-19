# https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    answer = 0
    while True:
        # (min, max)
        wallet = sorted(wallet)
        bill = sorted(bill)
        if bill[1] > wallet[1]:
            bill[1] = bill[1] // 2
            answer += 1
            continue
        if bill[0] > wallet[0]:
            bill[1] = bill[1] // 2
            answer += 1
            continue
        else:
            break
    print(wallet, bill) 
    return answer
