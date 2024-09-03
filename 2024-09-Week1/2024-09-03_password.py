# https://www.acmicpc.net/problem/4659

import sys
input = sys.stdin.readline

def aeiou(password):
    if set(password) & {'a','e','i','o','u'}:
        return True
    else:
        return False
    
def consecutive(password):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    cnt_v = 0
    cnt_c = 0

    for char in password:
        if char in vowels:
            cnt_v += 1
            cnt_c = 0
        else:
            cnt_c += 1
            cnt_v = 0            

        if cnt_c >= 3 or cnt_v >=3:
            return False
    return True

def same(password):
    for i in range(len(password)-1):
        a = password[i] 
        b = password[i+1]
        if a == b and a+b != "ee" and a+b != "oo" :
            return False
    return True



while True:
    password = input().rstrip()
    if password == "end":
        break
    else:
        if aeiou(password) and consecutive(password) and same(password):
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")