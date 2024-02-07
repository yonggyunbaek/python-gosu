# import sys

# N = int(input())
# scores=[list(map(int,input().split())) for _ in range(3)]
# sum_score=[0]*N

# for i in range(N):
#     axis_sum=0
#     for j in range(3):
#         axis_sum += scores[j][i]
#         # print(axis_sum)
#     sum_score.append(axis_sum)

# scores.append(sum_score)


# for score in scores:
#     rank = [sorted(score, reverse = True).index(s) + 1 for s in score]
#     print(' '.join(map(str,rank)))


# 위에꺼 시간초과

# 답 확인


# 점수리스트를 입력받아 각 점수에 대한 등수를 계산하자
def calculate_ranks(score_list):
    # 입력받은 점수 리스트를 (점수, 인덱스) 형태의 튜플로 변환, 점수 기준으로 내림차순 
    sorted_scores = sorted([(score, i) for i, score in enumerate(score_list)], reverse=True)
    print(f"sorted_scores: {sorted_scores}")
    # 등수를 저장할 리스트 초기화
    ranks = [0]*len(score_list)
    # 처음 등수, 이전 점수 초기화
    rank = 0
    prev_score = -1
    # 정렬된 점수 리스트 순회
    for i, (score, idx) in enumerate(sorted_scores):
        # 현재 점수가 이전 점수랑 다르면 idx + 1 로 등수 표현
        if score != prev_score:
            rank = i + 1
        # 원래 idx에 등수 넣기
        ranks[idx] = rank
        prev_score = score
        print(f"score: {score}, idx: {idx}, rank: {rank}, ranks: {ranks}")
    
    return ranks

N = int(input().strip())
scores = [list(map(int, input().strip().split())) for _ in range(3)]

# 입력 받은 스코어 리스트 랭크 리스트로
ranks = [calculate_ranks(score) for score in scores]

# 랭크 2차 리스트에서 순서대로 리스트 하나씩 space로 붙여서 출력
for rank in ranks:
    print(" ".join(map(str, rank)))

# score 자리별로 합계산(개인별 점수 합산)
total_scores = [sum(x) for x in zip(*scores)]
print(f"total_scores: {total_scores}")

# 개인별 점수 합산 랭크 확인
total_ranks = calculate_ranks(total_scores)
print(" ".join(map(str, total_ranks)))
