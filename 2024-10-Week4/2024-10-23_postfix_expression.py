import sys
from collections import deque
import operator
input = sys.stdin.readline

n = int(input())
postfix = list(input().rstrip())
# print(postfix)
num_dict = { chr(i):int(input()) for i in range(ord('A'),ord('A')+n) }
# {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

stack = deque()
for i in postfix:
    if num_dict.get(i):
        stack.append(num_dict[i])
    else:
        if stack:
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[i](b,a))

print( f'{stack[0]:.2f}' )