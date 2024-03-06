# 백준 28279

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deque = deque([])
result = None

for _ in range(N):
    lst = list(map(int, input().split()))
    # print(lst)
    if len(lst) == 2:
        if lst[0] == 1:
            deque.insert(0, lst[1])
        elif lst[0] == 2:
            deque.append(lst[1])
        continue
    else:
        if lst[0] == 3:
            if len(deque) == 0:
                result = -1
            else:
                result = deque.popleft()
        elif lst[0] == 4:
            if len(deque) == 0:
                result = -1
            else:
                result = deque.pop()
        elif lst[0] == 5:
            result = len(deque)

        elif lst[0] == 6:
            if len(deque) == 0:
                result = 1
            else:
                result = 0
        elif lst[0] == 7:
            if len(deque) != 0:
                result = deque[0]
            else:
                result = -1
        elif lst[0] == 8:
            if len(deque) != 0:
                result = deque[-1]
            else:
                result = -1
        print(result)

# 리스트 pop(0)는 제일 왼쪽 원소 삭제하고 모든 원소를 앞으로 이동 -> O(n)
# deque는 double-linked list로 구현되어 있고 양 끝의 요소의 추가/삭제 pop(), popleft()가 O(1)