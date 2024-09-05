import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def can_transform(s, t):
    # s와 t가 같으면 성공
    if s == t:
        return True
    # t의 길이가 s보다 짧으면 안됨
    if len(t) < len(s):
        return False
    
    # t의 마지막 문자가 'A'이면 'A'를 제거하고 재귀 호출
    if t[-1] == 'A':
        if can_transform(s, t[:-1]):
            return True
    # t의 첫 번째 문자가 'B'이면 'B'를 제거하고 뒤집어서 재귀 호출
    if t[0] == 'B':
        if can_transform(s, t[1:][::-1]):
            return True
    
    # 변환이 불가능하면 False 
    return False


print(1 if can_transform(s, t) else 0)
