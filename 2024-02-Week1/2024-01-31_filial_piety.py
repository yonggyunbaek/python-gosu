# 부모님 농사 땅 일구는 일 돕기
# 3*3 격자 땅 - 9칸 - 칸마다 숫자(높이)
# 1*3 크기 땅(가로 또는 세로 한줄) 같은 높이로 맞추는데 필요한 비용 - 1 1 3 일 경우 비용은 2

import sys 

def height_check(hlist):
    check = [ hlist.count(1), hlist.count(2), hlist.count(3) ]

    if 3 in check:
        answer = 0
    elif 2 in check: 
        answer = abs(check.index(2) - check.index(1))
    else:
        answer = 2

    return answer

def main():
    
    input_matrix = []
    for i in range(3):
        input_matrix.append(list(map(int,sys.stdin.readline().split())))

    transposed_matrix = list(map(list, zip(*input_matrix)))

    answer_list = []
    for hlist in input_matrix + transposed_matrix:
        answer_list.append(height_check(hlist))
    
    print(min(answer_list))
    


if __name__ == "__main__":
    main()

