# https://school.programmers.co.kr/learn/courses/30/lessons/12915

from collections import defaultdict
def solution(strings, n):
    string_dict = defaultdict(str)
    
    for s in strings:
        string_dict[s] = s[n]
    
    
    answer = sorted(string_dict, key=lambda x: (string_dict[x],x))
    return answer
