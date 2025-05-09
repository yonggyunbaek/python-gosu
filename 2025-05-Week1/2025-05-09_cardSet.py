# https://www.acmicpc.net/problem/11507

import sys
input = sys.stdin.readline

name = input().rstrip()
cnt={'P':13,'K':13,'H':13,'T':13}

cardset=set()

for i in range(0,len(name)-2, 3):
    if name[i:i+3] in cardset:
        print("GRESKA")
        break
    else:
        cardset.add(name[i:i+3])
    
    cnt[name[i]] -= 1

else:
    print(*list(cnt.values()))
