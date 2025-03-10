# https://www.acmicpc.net/problem/6550

import sys
input = sys.stdin.readline

while True:
    try:
        s,t = input().split()
        idx = 0
        for i in range(len(t)):
            if idx == len(s):
                break
            if s[idx] == t[i]:
                idx += 1
        
        print("Yes" if len(s) == idx else "No")
    except:
        break




        
    
