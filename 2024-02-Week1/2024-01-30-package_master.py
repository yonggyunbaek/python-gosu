# 택배 상하차 알바
# 택배가 내려오는 레일의 순서를 조작해 최소한의 무게만 들고싶다
# N개 레일
# N번째 레일의 택배무게 Ni
# 택배 바구니 무게 M 
# 바구니 무게 초과하지 않게 담아서 이동하면 1번 일한거
# K번 일할 때 최소한의 무게로 일하도록

# N M K
# N1 N2 N3...

import sys
import itertools

N,M,K = map(int,sys.stdin.readline().split())
Nlist = list(map(int, input().split()))

def cal_weight(T):
    current_sum = 0
    cnt = 0

    for i in range(K):
        basket = 0
        
        while True:
            basket += T[cnt]
            cnt = (cnt+1) % N  # 마지막 레일가면 다시 처음으로
            if basket + T[cnt] > M: # 다음 레일 택배 담았을때 바구니무게 초과하면 break
                break
        current_sum += basket
    return current_sum

def main():
    
    pmts = list(itertools.permutations(Nlist))
    answer_lst = []
    for i in pmts:
        answer_lst.append(cal_weight(i))

    print(min(answer_lst))


if __name__ == "__main__":
    main()
