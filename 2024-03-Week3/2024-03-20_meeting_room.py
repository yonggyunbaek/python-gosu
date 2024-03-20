import sys

room_num, meeting = map(int, input().split())

room_list = {}
for i in range(room_num):
    name = input()
    room_list[name] = [0] * 18

for i in range(meeting):
    name, start, end = input().split()
    start = int(start)
    end = int(end)
    for j in range(start, end):
        room_list[name][j] = 1

room_list = sorted(room_list.items())

for i in range(room_num):
    current = 1
    temp = []
    for j in range(9, 18):
        if current == 1 and room_list[i][1][j] == 0:
            sTime = j
            current = 0
        elif current == 0 and room_list[i][1][j] == 1:
            fTime = j
            current = 1
            temp.append([sTime, fTime])
    if current == 0:
        temp.append([sTime, 18])

    print(f'Room {room_list[i][0]}:')
    if len(temp) == 0:
        print('Not available')
    else:
        print(len(temp), 'available:')
        for j in range(len(temp)):
            print(f'{temp[j][0]:02d}-{temp[j][1]:02d}')
    if i != room_num - 1:
        print('-----')
