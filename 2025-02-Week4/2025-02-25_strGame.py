# https://www.acmicpc.net/problem/20437

from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input().rstrip()
    k = int(input())
    minv = len(w)+1
    maxv = -1
    alpha_dict = defaultdict(list)
    for i in range(len(w)):
        alpha_dict[w[i]].append(i)

    for idx_lst in alpha_dict.values():
        if len(idx_lst) < k:
            continue
        for i in range(len(idx_lst)-k+1):
            minv = min(minv, idx_lst[i+k-1]-idx_lst[i] +1 )
            maxv = max(maxv, idx_lst[i+k-1]-idx_lst[i] +1 )
    if maxv == -1:
        print(maxv)
    else:
        print(minv, maxv)
