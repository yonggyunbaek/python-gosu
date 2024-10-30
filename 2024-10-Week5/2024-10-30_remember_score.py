def solution(name, yearning, photo):
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]       
    answer = []
    for i in photo:
        ans = 0
        for j in i:
            if score.get(j):
                ans += score.get(j)
        answer.append(ans)
    return answer