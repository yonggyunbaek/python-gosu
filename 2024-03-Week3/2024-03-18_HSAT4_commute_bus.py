# https://softeer.ai/practice/6257
# 
# 레전드 설명 블로그 
# https://velog.io/@trillionaire/Softeer-%EC%9D%B8%EC%A6%9D%ED%8F%89%EA%B0%804%EC%B0%A8-%EA%B8%B0%EC%B6%9C-%ED%86%B5%EA%B7%BC%EB%B2%84%EC%8A%A4-%EC%B6%9C%EB%B0%9C-%EC%88%9C%EC%84%9C-%EA%B2%80%EC%A6%9D%ED%95%98%EA%B8%B0

import sys
import itertools

input = sys.stdin.readline

N = int(input())
numlst = list(map(int, input().split()))


##### 시간 초과 #####
# nCr = itertools.combinations(numlst,3)
# answer = []
# for i in nCr:
#     a, b, c = i[0], i[1], i[2]
#     if a < b and a > c:
#         answer.append(1)
#     else:
#         answer.append(0)

# print(sum(answer))
answer = []

for i in range(1, N+1):
    check = []
    if len(numlst) - i < 2:
        break
    else:
        for j in range(i+1, N+1):
            if numlst[i-1] < numlst[j-1]:
                check.append(True)
            else:
                check.append(False)
    answer.append(check)        
# print(answer)
cnt = 0      
     
for i in answer:
    T_cnt = 0 
    for j in i: 
        if j == True:
            T_cnt += 1
        else:
            cnt += T_cnt
print(cnt)