#https://school.programmers.co.kr/learn/courses/30/lessons/12934#

import re
def solution(n):
    # print(str(n**(1/2)))
    regex = r"^[0-9]*\.[0]$"
    if re.match(regex, str(n**(1/2))):
        # print(int(n**(1/2)+1)**2)
        return int(n**(1/2)+1)**2
    return -1
