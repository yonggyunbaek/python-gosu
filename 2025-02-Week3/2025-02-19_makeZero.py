# https://www.acmicpc.net/problem/7490

from itertools import product
import sys
input = sys.stdin.readline

t = int(input())
ops = ["+", "-", " "]
for _ in range(t):
    n = int(input())
    n_lst = list(range(1,n+1))
    answer = set()
    for ops_product in set(product(ops,repeat=n-1)):
        final = ''
        for i in range(len(ops_product)):
            final = final + str(n_lst[i]) + ops_product[i] 
        final += str(n_lst[-1])
        result = final.replace(" ","")
        check = eval(result)
        if check == 0:
            answer.add(final)
    print(*sorted(answer), sep="\n")
    print()