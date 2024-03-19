"""
문제

김교수는 강의실 1개에 최대한 많은 강의를 배정하려고 한다. 배정된 강의는 서로 겹치지 않아야 하며 수업시간의 길이와 상관없이 최대한 강의를 많이 배정하라. 단, 두 강의의 시작시간과 종료시간은 겹쳐도 된다.

제약조건
1≤N≤ 106 인 정수
1≤S<F=109

입력형식
첫 번째 줄에 강의 개수 N이 주어진다. i+ 1 (1 ≤i≤ N)번째 줄에는 i번째 강의의 시작 시간 S,와 종료 시간 F가 주어진다.

출력형식
첫 번째 줄에 최대 강의 수를 출력하라.
"""


# 풀이 1 / 메모리 초과 2개
import sys
"""
강의실 1개에 강의 배정, 겹치지 않게
최대한 강의 많이 배정
시작과 종료시간 겹쳐도 가능 >> 최대한 겹치게
"""

lecture_num = int(sys.stdin.readline())
lecture_list = [list(map(int,sys.stdin.readline().split())) for _ in range(lecture_num)]
# 강의 끝나는 시간 기준 정렬
lecture_list = sorted(lecture_list, key=lambda x: x[1])

max_lect = [lecture_list[0]]

for l in range(1,len(lecture_list)):

    if max_lect[-1][1] <= lecture_list[l][0]:
        max_lect.append(lecture_list[l])

print(len(max_lect))


# 풀이 2/ 통과
import sys

lecture_num = int(sys.stdin.readline())
lecture_list = [list(map(int,sys.stdin.readline().split())) for _ in range(lecture_num)]
lecture_list = sorted(lecture_list, key=lambda x: x[1])

max_lect_count = 1
end_time = lecture_list[0][1]# 첫 강의 끝나는 시간

for i in range(1, len(lecture_list)):
    if end_time <= lecture_list[i][0]: # 끝나는 시간, 시작시간 비교
        max_lect_count += 1
        end_time = lecture_list[i][1] #end_time update

print(max_lect_count)