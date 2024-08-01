def solution(n):
    watermelon = "수박"
    if n % 2 == 0:
        return "수박" * (n // 2)
    else:
        return "수박" * (n // 2) + "수"
