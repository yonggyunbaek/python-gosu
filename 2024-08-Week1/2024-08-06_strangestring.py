# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s_list = s.split(' ')
    ans = []
    for ele in s_list:
        answer = ''
        for i, char in enumerate(ele):
            if i % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
        ans.append(answer)
    return ' '.join(ans)
