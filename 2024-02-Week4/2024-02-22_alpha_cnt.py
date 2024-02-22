# 백준 1157

word_alpha = list(input().upper())

dict = {}
for i in word_alpha:
    if i in dict:
        continue
    else:
        dict[i] = word_alpha.count(i)

max_val = max(dict.values())
answer_lst = [ k for k,v in dict.items() if v == max_val ]

if len(answer_lst) == 1:
    print(answer_lst[0])
else:
    print('?')