# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer, score_board = [], []
    """
    1~k일까지는 모든 점수가 명예의 전당
    k+1 일 부터는 줄세우고 k개만 등록
    매일 최하위 점수 answer 반환
    """
    for s in score:
        if len(score_board) == k:
            min_score = min(score_board)
            if min_score < s:
                score_board.remove(min_score)
                score_board.append(s)
        else:
            score_board.append(s)

        answer.append(min(score_board))
    return answer
