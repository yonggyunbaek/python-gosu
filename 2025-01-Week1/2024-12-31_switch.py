# https://www.acmicpc.net/problem/1244

import sys
input = sys.stdin.readline

def symmetry(idx:int, switch:list):
    cnt = 1
    while idx + cnt < len(switch) and idx - cnt > 0:
        left = idx - cnt
        right = idx + cnt
        if switch[left] == switch[right]:
            switch[left] = 1- switch[left]
            switch[right] = 1- switch[right]
            cnt += 1
        else:
            return switch
    return switch


n = int(input())
switch = [0] + list(map(int, input().split()))
studentN = int(input())

for _ in range(studentN):
    sex, num = map(int, input().split())
    if sex == 1:
        cnt = 1
        while num*cnt < len(switch):
            # 1, 0 반전시키기
            switch[num*cnt] = 1- switch[num*cnt]
            cnt += 1
    else:
        switch[num] = 1- switch[num]
        switch = symmetry(num, switch)

if len(switch) // 20 == 0:
    print(*switch[1:])
else:
    for i in range(len(switch) // 20 + 1):
        print(*switch[20*i+1:20*(i+1)+1])
