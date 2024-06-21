# https://www.acmicpc.net/problem/10825

# 판다스 #
# import sys
# import pandas as pd
# input = sys.stdin.readline

# N = int(input())

# data = [ list(input().rstrip().split()) for _ in range(N) ]
# # print(data)

# df = pd.DataFrame(data, columns= ['name', 'kor', 'eng', 'math'])
# df = df.astype({'kor':'int64', 'eng':'int64', 'math':'int64'})
# # print(df.dtypes)
# df = df.sort_values(by=['kor', 'eng', 'math', 'name'], ascending=[False, True, False, True])

# answer = df['name'].tolist()
# print('\n'.join(answer))

import sys
input = sys.stdin.readline

N = int(input())
data = [ list(input().rstrip().split()) for _ in range(N) ]
data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
print(data)

for i in data:
    print(i[0])