import sys

N = int(input())
input_lst = [ list(sys.stdin.readline().split()) for _ in range(N) ]
# [['Exit', 'A1in'], ['Axis', 'A0on'], ['Exam', 'Star'], ['WKXM', 'XHHV'], ['maxB', 'pyht'], ['XBut', 'Club'], ['ATax', 'Keep'], ['ifXY', 'doC2']]

ans_lst = []
for i in input_lst:
    idx = i[0].find('x')
    if idx == -1:
        idx = i[0].find('X')
    print(idx)
    ans_lst.append(i[1][idx].upper())

print(''.join(ans_lst))