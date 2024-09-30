# https://www.acmicpc.net/problem/2941

import sys
input = sys.stdin.readline

word = input().rstrip()
s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for i in s:
    cnt += word.count(i)
    word = word.replace(i, '1')
    # print(word, cnt)
cnt += len(word)
cnt -= word.count('1')
print(cnt)
    
