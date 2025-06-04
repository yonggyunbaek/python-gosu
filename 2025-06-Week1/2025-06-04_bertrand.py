# https://www.acmicpc.net/problem/4948

import sys
import time
input = sys.stdin.readline


# def isPrimeNumber(n):
#     for i in range(2, int(n**(1/2))+1):
#         if n % i == 0:
#             return False
#     return True

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 0
#     for i in range(n+1, 2*n+1):
#         if isPrimeNumber(i):
#             cnt += 1
#     print(cnt)

def isPrimeNumber(n):
    arr = [True] * (n + 1) 
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True: 
            j = 2

            while (i * j) <= n:
                arr[i*j] = False 
                j += 1

    return arr

while True:
    n = int(input())
    if n == 0:
        break
    
    print(isPrimeNumber(2*n).count(True) - isPrimeNumber(n).count(True))
