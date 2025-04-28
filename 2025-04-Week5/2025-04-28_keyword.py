# https://www.acmicpc.net/problem/22233

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
keyword = set(input().rstrip() for _ in range(n))

# 시간 초과
# 차집합 연산 O(최소 set 크기) 이므로 set이 클수록 오래걸림
# tmp = set()
# for _ in range(m):
#     write = set(input().rstrip().split(","))
#     write = write - tmp
#     tmp = write
#     keyword = keyword - write
#     print(len(keyword))

tmp = set()
for _ in range(m):
    words = input().rstrip().split(",")
    # 단어 하나씩 처리
    for w in words:
        # tmp에 없으면 추가
        if w not in tmp:
            tmp.add(w)
            # tmp에 없고 키워드에 있으면 키워드에서 제거
            if w in keyword:
                keyword.remove(w)
    print(len(keyword))