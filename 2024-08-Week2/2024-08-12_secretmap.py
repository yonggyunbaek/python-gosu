# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        or_oper = bin(a1 | a2)[2:]
        if len(or_oper) != n:
            or_oper = (n - len(or_oper)) * '0' + or_oper
        print(or_oper)
        
        tmp = ''
        for o in or_oper:
            if o == '1':
                tmp += '#'
            if o == '0':
                tmp += ' '
        answer.append(tmp)
    # print(answer)
    return answer
