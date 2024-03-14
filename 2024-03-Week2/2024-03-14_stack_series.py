# https://www.acmicpc.net/problem/1874

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numlst = [ int(input()) for _ in range(N) ]



def make_series(numlst):
    current = 1
    series = deque()
    answer_lst = []
    for i in numlst:
        # current 1씩 커지면서 확인하면 기존 숫자 처리 가능
        while i >= current:
            series.append(current)
            answer_lst.append("+")
            current += 1
        # 숫자 빼낼때 주어진 수열과 비교 해서 다르면 수열 못만드니까 NO
        if series[-1] == i:
            series.pop()
            answer_lst.append("-")
        else:
            return "NO"
    return "\n".join(answer_lst)

result = make_series(numlst)
print(result)




