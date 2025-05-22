# https://www.acmicpc.net/problem/22859

import re

source = input()


main = re.findall('<main>(.*)</main>', source)[0]
divList = re.findall('<div title="(.*?)">(.*?)</div>', main)

for title, paragraph in divList:
    print('title :' , title)
    paraList = re.findall('<p>(.*?)</p>', paragraph)
    for p in paraList:
        # re.sub(pattern, replacement, string)
        # <...> 없애기
        p = re.sub('(<.*?>)', '', p)
        # 하나이상의 공백문자 제거
        p = re.sub('\s+', ' ', p.strip())
        print(p)
    

