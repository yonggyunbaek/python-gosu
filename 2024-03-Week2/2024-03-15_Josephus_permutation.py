# https://www.acmicpc.net/problem/1158

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

numlst = list(range(1,N+1))
# print(numlst)
idx = 0
answer = []
while numlst:
    if len(numlst) >= K:
        idx = K - 1
        answer.append(numlst[idx])
        numlst = [ numlst[i] for i in range(idx+1, len(numlst)) ] + [ numlst[i] for i in range(idx) ]
    elif K -len(numlst) - 1 < len(numlst):
        idx = K -len(numlst) - 1
        # print(numlst)
        # print(idx)
        answer.append(numlst[idx])
        numlst = [ numlst[i] for i in range(idx+1, len(numlst)) ] + [ numlst[i] for i in range(idx) ]
    else:
        idx = K % len(numlst) - 1
        if idx == -1:
            answer.append(numlst[idx])
            numlst.remove(numlst[idx])
        else:
            answer.append(numlst[idx])
            numlst = [ numlst[i] for i in range(idx+1, len(numlst)) ] + [ numlst[i] for i in range(idx) ]

    # print("numlst", numlst)
    # print("answer", answer)

print("<",end='')
print(*answer, sep=', ', end='')
print(">")



