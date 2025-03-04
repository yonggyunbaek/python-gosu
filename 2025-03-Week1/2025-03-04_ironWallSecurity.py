# https://www.acmicpc.net/problem/9322

from collections import defaultdict
import sys
input = sys.stdin.readline

def idx(pubkey:list, n):
    idx = defaultdict(int)
    for i in range(n):
        idx[pubkey[i]] = i
    return idx

t = int(input())
for _ in range(t):
    n = int(input())
    pubkey1 = list(input().split())
    pubkey2 = list(input().split())
    sentence = list(input().split())
    
    pkidx1 = idx(pubkey1,n)
    pkidx2 = idx(pubkey2,n)
    moveidx = []
    for i in pubkey1:
        moveidx.append((pkidx2[i],pkidx1[i]))

    answer = [ "A" ] * n
    for before, after in moveidx:
        answer[after] = sentence[before]
    print(*answer)

