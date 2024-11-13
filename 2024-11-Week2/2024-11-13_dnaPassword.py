# https://www.acmicpc.net/problem/12891

import sys
from collections import Counter

input = sys.stdin.readline

def main():
    # 입력 받기
    s, p = map(int, input().split())
    password = list(input().rstrip())
    strcnt = list(map(int, input().split()))
    dna = ['A', 'C', 'G', 'T']
    strCntDict = {dna[i]: strcnt[i] for i in range(4)}

    # 현재 윈도우 내 각 문자들의 개수를 저장할 딕셔너리
    window_cnt = {ch: 0 for ch in dna}
    
    # 초기 윈도우 설정
    for i in range(p):
        window_cnt[password[i]] += 1
    
    # 조건을 만족하는지 확인하는 함수
    def isValid():
        for ch in dna:
            if window_cnt[ch] < strCntDict[ch]:
                return False
        return True
    
    cnt = 0
    
    # 첫 번째 윈도우 검사
    if isValid():
        cnt += 1
    
    # 초기 윈도우는 인덱스 0 ~ p-1까지 확인 했으니까
    # 인덱스p 부터 끝(s-1)까지 슬라이딩 윈도우로 검사
    for i in range(p, s):
        # 맨끝 새로운 문자가 들어옴
        window_cnt[password[i]] += 1
        # 맨앞 오래된 문자가 나감
        window_cnt[password[i - p]] -= 1
        

        if isValid():
            cnt += 1
    
    return cnt

print(main())
