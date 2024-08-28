# https://school.programmers.co.kr/learn/courses/30/lessons/131128

# from collections import Counter

# def solution(X, Y):
#     X_counter = Counter(X)
#     Y_counter = Counter(Y)
    
#     # 공통 숫자를 찾고, 최대 개수만큼 리스트에 추가
#     co_num = []
#     for k in (X_counter & Y_counter).elements():
#         co_num.append(k)

#     if not co_num:
#         return "-1"
    
#     # 결과를 정렬하고, 정수로 변환하여 문자열로 반환
#     answer = ''.join(sorted(co_num, reverse=True))
#     return str(int(answer))
def solution(X, Y):
    # 각 숫자의 개수를 세기 위한 리스트 (0부터 9까지)
    count_X = [0] * 10
    count_Y = [0] * 10
    
    # X와 Y에서 각 숫자의 개수를 세기
    for char in X:
        count_X[int(char)] += 1
    for char in Y:
        count_Y[int(char)] += 1
    
    # 공통 숫자를 저장할 리스트
    co_num = []
    
    # 공통된 숫자와 그 개수를 찾기
    for i in range(9, -1, -1):  # 9부터 0까지
        common_count = min(count_X[i], count_Y[i])
        co_num.extend([str(i)] * common_count)  # 공통된 숫자 추가
    
    if not co_num:
        return "-1"
    
    # 리스트를 문자열로 변환
    answer = ''.join(co_num)
    
    # 숫자가 0으로만 구성된 경우 처리
    return answer if answer != '0' * len(answer) else '0'
