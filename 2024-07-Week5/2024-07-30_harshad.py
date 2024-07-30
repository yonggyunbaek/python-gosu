def solution(x):
    harshad = 0
    for n in str(x):
        harshad += int(n)
    
    if x % harshad == 0:
        return True
    else:
        return False