# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # print(i-1,j-1,k-1)
        slice_array = array[i-1:j]
        slice_array = sorted(slice_array)
        # print(slice_array)
        answer.append(slice_array[k-1])
    
    return answer
