"""
문제
N명의 학생들의 성적이 학번순서대로 주어졌다.
학번 구간 [A, B]가 주어졌을 때 이 학생들 성적의 평균을 구하는 프로그램을 작성하라.

제약조건

1≤N≤106인 정수
1≤K≤104인 정수
1≤S ≤ 100 인 정수
1SASB=N

입력형식
첫 번째 줄에 학생 수 N과 구간 수 K가 주어진다.
두 번째 줄에는 학생의 성적 S1 (1 ≤i≤ N)가 주어진다. i + 2 (1 ≤i≤ K)번째 줄에는 i번째 구간 Ay, B가 주어진다.
"""

import sys

n, k = map(int, sys.stdin.readline().split())
score = list(map(int,sys.stdin.readline().split()))

for _ in range(k):
    left, right = map(int,sys.stdin.readline().split())
    sum = 0
    for n in score[left-1:right]:
        sum += n
    print(format(round(sum/(right-left+1),2),".2f"))