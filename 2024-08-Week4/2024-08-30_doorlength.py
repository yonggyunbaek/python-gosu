# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0

    dx = [0, 0, 1, -1]      # U D R L
    dy = [1, -1, 0, 0]

    cur_x, cur_y = 0, 0

    door = []

    for d in dirs:
        if d == 'U':
            next_x, next_y = cur_x + dx[0], cur_y + dy[0]
        elif d == 'D':
            next_x, next_y = cur_x + dx[1], cur_y + dy[1]  
        elif d == 'R':
            next_x, next_y = cur_x + dx[2], cur_y + dy[2]  
        elif d == 'L':
            next_x, next_y = cur_x + dx[3], cur_y + dy[3]  

        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            px = cur_x
            py = cur_y
            cur_x = next_x
            cur_y = next_y
            if [px, cur_x, py, cur_y] not in door and [cur_x, px, cur_y, py] not in door:
                door.append([px, cur_x, py, cur_y])
        else:
            next_x = cur_x
            next_y = cur_y

    return len(door)
