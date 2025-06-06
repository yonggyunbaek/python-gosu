# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

f = input().split('-') #'-'를 기준으로 split

num = [] #'-'로 나눈 항들의 합을 저장할 리스트

for i in f:
    sum = 0
    tmp = i.split('+') #덧셈을 하기 위해서 '+'를 기준으로 split
    for j in tmp: #split한 리스트의 각 요소들을 더해줌
        sum += int(j)
    num.append(sum) #각 항의 덧셈 결과를 num에 저장

n = num[0] #식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다

for i in range(1,len(num)): #1번째 값부터 n에서 빼준다
    n -= num[i]
print(n)