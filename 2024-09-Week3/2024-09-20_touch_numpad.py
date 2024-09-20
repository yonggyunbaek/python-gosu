# https://school.programmers.co.kr/learn/courses/30/lessons/67256

keypad_coordinates = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    '*': (3, 0),
    0: (3, 1),
    '#': (3, 2)
}

def touch_num(hand_loc, num, hand):
    if num in [1, 4, 7]:
        hand_loc[0] = num
        return "L"
    elif num in [3, 6, 9]:
        hand_loc[1] = num
        return "R"
    else:
        # 맨해튼 거리 계산
        l = abs(keypad_coordinates[num][0] - keypad_coordinates[hand_loc[0]][0]) + \
            abs(keypad_coordinates[num][1] - keypad_coordinates[hand_loc[0]][1])
        r = abs(keypad_coordinates[num][0] - keypad_coordinates[hand_loc[1]][0]) + \
            abs(keypad_coordinates[num][1] - keypad_coordinates[hand_loc[1]][1])
        
        if l < r:
            hand_loc[0] = num
            return 'L'
        elif l > r:
            hand_loc[1] = num
            return 'R'
        else:  # l == r
            if hand == 'left':
                hand_loc[0] = num
                return 'L'
            else:
                hand_loc[1] = num
                return 'R'

def solution(numbers, hand):
    answer = []
    hand_loc = ['*', '#']  # [left, right]
    
    for n in numbers:
        ans = touch_num(hand_loc, n, hand)
        answer.append(ans)
    
    return ''.join(answer)
