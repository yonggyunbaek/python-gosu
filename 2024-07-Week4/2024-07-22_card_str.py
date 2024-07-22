# https://www.acmicpc.net/problem/13417

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    card = list(input().split())
    ans =''
    for i in range(N):
        if i == 0:
            ans += card[i]
        else:
            if card[i] <= ans[0]:
                ans = card[i] + ans
            elif card[i] > ans[0]:
                ans = ans + card[i]

    print(ans)
