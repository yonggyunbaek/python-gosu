"""
문제

현대자동차에서는 부드럽고 빠른 변속이 가능한 8단 습식 DCT 변속기를 개발하여 N라인 고성능차에 적용하였다. 관련하여 SW 엔지니어인 당신에게 연속적으로 변속이가능한지 점검할 수 있는 프로그램을 만들라는 임무가 내려왔다.

당신은 변속기가 1단에서 8단으로 연속적으로 변속을 한다면 ascending, 8단에서 1단으로 연속적으로 변속한다면 descending, 둘다 아니라면 mixed 라고 정의했다.

변속한 순서가 주어졌을 때 이것이 ascending인지, descending인지, 아니면mixed인지 출력하는 프로그램을 작성하시오.
"""

import sys

input_num = sys.stdin.readline().split() # list

# input_num is list,

if sorted(input_num) == input_num:
    print("ascending")
elif sorted(input_num, reverse=True) == input_num:
    print("descending")
else:
    print("mixed")
    
    