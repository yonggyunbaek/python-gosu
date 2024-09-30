# https://school.programmers.co.kr/learn/courses/30/lessons/68936?language=python3

def solution(arr):
    answer = [0, 0]  # [0의 개수, 1의 개수]
    n = len(arr)
    
    def check(arr, x, y, size):
        value = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != value:
                    return False
        return True
    
    def quad_comp(arr, x, y, size):
        if check(arr, x, y, size):
            answer[arr[x][y]] += 1  # 0 또는 1의 개수를 카운트
            return
        
        half_size = size // 2
        quad_comp(arr, x, y, half_size)
        quad_comp(arr, x + half_size, y, half_size)
        quad_comp(arr, x, y + half_size, half_size)
        quad_comp(arr, x + half_size, y + half_size, half_size)
    
    quad_comp(arr, 0, 0, n)
    return answer
