# https://www.acmicpc.net/problem/10769

import sys
input = sys.stdin.readline

i = input().rstrip()
happy = i.count(":-)")
sad = i.count(":-(")

if happy == 0 and sad ==0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')