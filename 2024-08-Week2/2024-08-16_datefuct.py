# https://school.programmers.co.kr/learn/courses/30/lessons/12901

from datetime import date
def solution(a, b):
    date_dict = {
        0 : 'MON',
        1 : 'TUE',
        2 : 'WED',
        3 : 'THU',
        4 : 'FRI',
        5 : 'SAT',
        6 : 'SUN'
    }
    # print(date(2016,5,24).weekday())
    weekday = date(2016,a,b).weekday()
    return date_dict[weekday]
