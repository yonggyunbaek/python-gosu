# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    # ext : extract element
    # val_ext : valid number (less than)
    # sort_by : sorting key
    sort_key = {"code" : 0,
                "date" : 1,
                "maximum" : 2,
                "remain" : 3
               }
    
    for d in data:
        # print(d[0],d[1],d[2],d[3])
        if d[sort_key[ext]] < val_ext:
            answer.append(d)
        else:
            continue
    # print(answer)
    answer = sorted(answer, 
                    key=(lambda x: x[sort_key[sort_by]]))
    return answer
