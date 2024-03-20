# https://www.acmicpc.net/problem/1620


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

book = {}
for i in range(N):
    pokemon = input().strip()
    book.update( {str(i+1):pokemon} )
    book.update( {pokemon:str(i+1)} )

check = [ input().strip() for _ in range(M) ]

for i in check:
    print(book.get(i))


### 시간 초과 ###
# reverse_dict 만드는 시점에 for 때문에 
    
# N, M = map(int, input().split())

# dict = { i+1:input().strip() for i in range(N) }

# check = [ input().strip() for _ in range(M) ]

# for i in check:
#     if i.isdigit():
#         key = int(i)
#         print(dict.get(key))
#     else:
#         reverse_dict = {v: k for k, v in dict.items()}
#         print(reverse_dict.get(i))