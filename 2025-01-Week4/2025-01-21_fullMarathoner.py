# https://www.acmicpc.net/problem/10546

from collections import defaultdict
import sys
input = sys.stdin.readline

### 시간 초과 ### 
# n = int(input())
# participants = [ input().rstrip() for _ in range(n) ]
# for _ in range(n-1):
#     participants.remove(input().rstrip())
# print(participants[0])


n = int(input())
p = defaultdict(int)
for _ in range(n):
    p[input().rstrip()] += 1

for _ in range(n-1):
    p[input().rstrip()] -= 1

answer = [k for k, v in p.items() if v == 1]
print(answer[0])