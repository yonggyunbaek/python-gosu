import sys

N = int(input())
scores=[list(map(int,input().split())) for _ in range(3)]

sum_score=[]
for i in range(N):
    axis_sum=0
    for j in range(N):
        axis_sum += scores[j][i]
        print(axis_sum)
    sum_score.append(axis_sum)


scores.append(sum_score)
print(scores)
for score in scores:
    rank = [sorted(score, reverse = True).index(s) + 1 for s in score]
    print(' '.join(map(str,rank)))



