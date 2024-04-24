# https://www.acmicpc.net/problem/2910

import sys
from collections import Counter

input = sys.stdin.readline

N, C = map(int, input().split())
numlst = list(map(int, input().split()))

cnt_dict = dict(Counter(numlst))
# sorted는 stable sort여서 기존 리스트 순서 유지 가능
# 두번째 요소 기준 내림차순
cnt = sorted(cnt_dict.items(), key=lambda x : -x[1])
# 딕셔너리 키 기준 정렬
# cnt = sorted(cnt_dict.items(), reverse = True)
print(cnt)
answer = []
for a,b in cnt:
    answer += [str(a)]*b

print(' '.join(answer))