def solution(s):
    if len(s) % 2 == 0: # even
        mid = len(s) // 2 - 1
        return s[mid:mid+2]
    else: # odd
        mid = len(s) // 2
        return s[mid]
