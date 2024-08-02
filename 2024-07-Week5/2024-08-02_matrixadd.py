def solution(arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1,arr2):
        tmp = [e1 + e2 for e1, e2 in zip(a1, a2)]
        answer.append(tmp)
    return answer
