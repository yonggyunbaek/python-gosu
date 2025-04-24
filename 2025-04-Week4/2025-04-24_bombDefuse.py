# https://www.acmicpc.net/problem/9242

import sys
input = sys.stdin.readline

nums = []

for i in range(5):
    a = input()[:-1]
    if len(a) % 4 != 3:
        continue
    row = []
    for j in range(0,len(a)+1,4):
        tmp = a[j:j+3]
        v = 0
        if tmp[0] == '*':
            v += 1
        if tmp[1] == '*':
            v += 2
        if tmp[2] == '*':
            v += 4
        row.append(v)
    nums.append(row)

if len(nums) == 0:
    print("BOOM!!")
    sys.exit()

nums = list(zip( *nums ))

samples = { (7,5,5,5,7):'0', (4,4,4,4,4):'1', (7,4,7,1,7):'2', (7,4,7,4,7):'3', (5,5,7,4,4):'4', (7,1,7,4,7):'5', (7,1,7,5,7):'6', (7,4,4,4,4):'7', (7,5,7,5,7):'8', (7,5,7,4,7):'9' }

answer = ''
for n in nums:
    if n in samples:
        answer += samples[n]
    else:
        print("BOOM!!")
        break
else:
    if int(answer) % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")