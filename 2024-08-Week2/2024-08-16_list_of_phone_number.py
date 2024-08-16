# https://www.acmicpc.net/problem/5052
import sys
input = sys.stdin.readline

def check(pn_list):
    # 사전 순으로 정렬하게 되면 접두어가 되는 전화번호는 항상 인접하게 위치 ->  바로 다음 번호만 확인하면 됨
    pn_list.sort()
    # 문자열 길이로 정렬할 필요없음 
    # pn_list.sort(key = lambda x: len(x))
    for i in range(len(pn_list)-1):
        if pn_list[i] == pn_list[i+1][:len(pn_list[i])]:
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())
    pn_list = [ input().rstrip() for _ in range(n) ]
    
    print(check(pn_list))





