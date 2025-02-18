# https://www.acmicpc.net/problem/1270

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    data = list(map(int,input().split()))
    soldier_all = data[0]
    
    # O(NlogN)
    # soldier_num_cnt = Counter(data[1:])
    # snc = [ (v, k) for k, v in soldier_num_cnt.items() ]
    # maxv, maxk = sorted(snc)[-1]

    soldiers = data[1:]
    soldier_count = {}
    maxv = 0
    maxk = -1

    for soldier in soldiers:
        if soldier in soldier_count:
            soldier_count[soldier] += 1
        else:
            soldier_count[soldier] = 1

        # 최대값을 바로 갱신
        if soldier_count[soldier] > maxv:
            maxv = soldier_count[soldier]
            maxk = soldier    

    if maxv > soldier_all // 2:
        print(maxk)
    else:
        print("SYJKGW")