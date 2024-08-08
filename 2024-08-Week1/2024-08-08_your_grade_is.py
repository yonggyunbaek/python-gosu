# https://www.acmicpc.net/problem/25206

import sys
input = sys.stdin.readline

report = []
score = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}
for _ in range(20):
    a,b,c = input().split()
    if c == 'P':
        continue
    else:
        report.append([float(b), score[c]])

grade_sum = 0
credit_sum = 0
for credit, grade in report:
    grade_sum += (credit*grade)
    credit_sum += credit
    # print(grade_sum,credit_sum)
    

print(round(grade_sum/credit_sum,6))