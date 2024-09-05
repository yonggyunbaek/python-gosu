# https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3
def solution(friends, gifts):
    # 친구 이름과 인덱스를 매핑하기 위한 딕셔너리
    friend_map = {friends[i]: i for i in range(len(friends))}
    index = [0] * len(friends)
    record = [[0] * len(friends) for _ in range(len(friends))]

    # 선물 기록을 처리
    for gift in gifts:
        giver, receiver = gift.split()
        giver_index = friend_map[giver]
        receiver_index = friend_map[receiver]
        index[giver_index] += 1
        index[receiver_index] -= 1
        record[giver_index][receiver_index] += 1

    # 다음 달에 받을 선물 수 계산
    ans = 0
    for i in range(len(friends)):
        cnt = 0
        for j in range(len(friends)):
            if i == j:
                continue
            if record[i][j] > record[j][i]:
                cnt += 1
            elif record[i][j] == record[j][i] and index[i] > index[j]:
                cnt += 1
        ans = max(cnt, ans)

    return ans
