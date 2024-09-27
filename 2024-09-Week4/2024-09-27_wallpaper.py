# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    min_x, min_y, max_x, max_y = len(wallpaper), len(wallpaper), 0, 0
    cnt = 0
    for y, wall in enumerate(wallpaper):
        for x, w in enumerate(wall):
            if w == '#' and cnt == 0:
                min_x, min_y = x, y
                cnt += 1
            if w == '#' and cnt != 0:
                min_x = min(min_x, x)
                max_x, max_y = max(max_x, x+1), max(max_y, y+1)
            else:
                continue
    answer = [min_y, min_x, max_y, max_x]
    return answer
