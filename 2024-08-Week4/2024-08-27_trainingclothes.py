# https://school.programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    student = [1] * n
    
    for l in lost:
        student[l - 1] -= 1
    # print(student)
    for r in reserve:
        student[r-1] += 1
    # print(student)
    for r in reserve:
        index = r - 1
        if student[index] == 2:
                # 왼쪽 학생에게 체육복 빌려주기
            if index > 0 and student[index - 1] == 0:
                student[index - 1] += 1
                student[index] -= 1
                continue
            # 오른쪽 학생에게 체육복 빌려주기
            if index < n - 1 and student[index + 1] == 0:
                student[index + 1] += 1
                student[index] -= 1
    print(student)
    return len(student) - student.count(0)
