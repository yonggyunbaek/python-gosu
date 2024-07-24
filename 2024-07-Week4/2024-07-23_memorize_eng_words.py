# https://www.acmicpc.net/problem/20920

import sys
from collections import defaultdict
N, M = map(int,input().split())

##################################
# 시간초과
# words = dict()
# for _ in range(N):
#     word = input().rstrip()
#     if len(word) >= M:
#         if word in words:
#             words[word] += 1
#         else:
#             words[word] = 1

## words.items() 로 key, balue가 tuple로 들어있는 리스토로 만들어서 정렬
# words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# print(words)
# for i in words:
#     print(i[0])
##################################

# defaultdict를 사용하여 키 존재 여부 확인을 제거 - 키가 존재하지 않을때 자동으로 기본값을 생성 - int로 하면 0이 기본값
words = defaultdict(int)

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        words[word] += 1

# 정렬 키 함수를 미리 정의 - lambda 생성 오버헤드 줄이기
def sort_key(item):
    return (-item[1], -len(item[0]), item[0])

# 정렬 후 바로 출력
for word, _ in sorted(words.items(), key=sort_key):
    print(word)