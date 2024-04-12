# https://www.acmicpc.net/problem/11478

import sys

S = list(sys.stdin.readline().strip())
answer = set()
for i in range(len(S)):
    sub_str=""
    for j in range(i,len(S)):
        # if S[i:j] != []:
            # answer.add(''.join(S[i:j]))
        sub_str += S[j]
        print(sub_str)
        answer.add(sub_str)
        print(answer)


print(len(answer))