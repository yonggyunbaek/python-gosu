# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
import ast
input = sys.stdin.readline

def main():
    p = list(input().rstrip())
    n = int(input())
    nums = deque(ast.literal_eval(input().rstrip()))

    reverse_flag = False  # reverse 상태 추적 (True: 뒤집어진 상태, False: 원래 상태)

    for cmd in p:
        if cmd == 'R':
            reverse_flag = not reverse_flag  # 상태를 반전
        else:  # 'D'
            if not nums: 
                return 'error'
            if reverse_flag: 
                nums.pop()
            else: 
                nums.popleft()

    # reverse 상태가 True이면 리스트 뒤집기
    if reverse_flag:
        nums.reverse()

    return list(nums)

if __name__ == "__main__":
    t = int(input()) 
    for _ in range(t):
        result = main()
        if result == 'error':
            print(result)
        else:
            # 리스트로 출력하면 comma 다음에 space들어가서 오답
            # print(list(result))
            print(f"[{','.join(map(str, result))}]")
