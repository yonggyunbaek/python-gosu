# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    stack = []

    for item in ingredient:
        stack.append(item)  # 재료를 스택에 추가
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # "1231" 제거
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1

    return answer


# def solution(ingredient):
#     answer = 0
    
#     ingred = ''.join(map(str,ingredient))
#     while True:
#         if "1231" in ingred:
#             ingred = ingred.replace("1231","",1)
#             answer += 1
#         else:
#             break
#     return answer
