# 연탄의 크기
# 산타가 연탄 배달 
# 난로와 연탄 모두 원 모양 / 난로의 반지름길이가 연탄의 반지름 길이의 배수인 집만 가능
# n개의 집
# 각 집의 반지름이 공백을 사이에 두고 주어짐
# 6
# 2 4 6 9 12 18

import sys


# 약수 구하기 
def divisor(n):
    divisor_lst = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i) == 0:
            divisor_lst.append(i)
            if (i**2) != n:
                divisor_lst.append(n // i)

    return divisor_lst

def main():
    n = int(input())
    radius_lst = map(int, sys.stdin.readline().split())
    accumulate_divsor_lst = []

    for i in radius_lst:
        accumulate_divsor_lst.extend(divisor(i))
    # print(accumulate_divsor_lst)
    answer_dict = {}
    for i in accumulate_divsor_lst:
        if i != 1:
            if i not in answer_dict.keys():
                answer_dict[i]=1
            else:
                answer_dict[i]+=1
    # print(answer_dict)
    print(max(answer_dict.values()))

if __name__ == "__main__":
    main()
    