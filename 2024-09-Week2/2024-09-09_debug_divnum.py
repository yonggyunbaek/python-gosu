#https://school.programmers.co.kr/learn/courses/30/lessons/340205
## orig Code
number = int(input())

answer = 0

for i in range(1):
    answer += number % 100
    number //= 100

print(answer)


## Debug Code
number = int(input())

answer = 0

for i in range(len(str(number))//2):
    answer += number % 100
    number //= 100

print(answer)
