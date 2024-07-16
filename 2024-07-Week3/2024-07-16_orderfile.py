# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re
from collections import defaultdict
def solution(files):
    files_dict = defaultdict(list)
    
    for f in files:
        orderby = [f.split(re.findall('\d+', f)[0])[0].lower(),int(re.findall('\d+', f)[0])]
        files_dict[f] = orderby
    print(files_dict)
    answer = sorted(files_dict, key=lambda x: (files_dict[x][0],files_dict[x][1]))
    print(answer)
    return answer
