# https://www.acmicpc.net/problem/1043

# 입력으로 주어지는 파티별 참석 인원은 입력 순서에 영향이없다
# 나중에 진실을 알게 되더라도 과장한 걸 걸리니까 

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
true_person = list(map(int,input().split()))
parties = []
for _ in range(M):
    # 파티 참석 리스트 저장
    parties.append(list(map(int,input().split()))[1:])
# 진실을 아는 사람 번호 리스트
knowlist = set(true_person[1:])

def cnt_party(M, true_person):   
    if len(true_person) == 1:
        cnt = M
        return cnt
    cnt = 0
    
    # 입력 순서 영향 없도록 knowlist 업데이트
    # 파티 수 만큼 반복체크
    for _ in range(M):
        for party in parties:
            # 파티 참가 인원 번호리스트 하나씩 집합으로 
            y = set(party)
            if knowlist & y:
                knowlist.update(y)
    
    for party in parties:
        y = set(party)
        if not knowlist & y:
            cnt += 1
    return cnt

answer = cnt_party(M, true_person)
print(answer)




