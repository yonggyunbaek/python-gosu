# 어버이날 선물을 사기위해 게임에 참가한다 (무궁화 꽃이 피었습니다)
# 남우는 처음에 술래랑 d만큼 거리
# 술래는 a초간 뒤를 보고 b초간 앞을 보고 a,b 반복..
# 남우가 술래 터치하면 b초 앞보고 a초 뒤보고 b,a 반복..
# 남우는 초당 1만큼 이동
# 남우가 술래 터치하고 출발지 돌아오는데 걸리는 시간

import sys

a, b, d = map(int, sys.stdin.readline().split())

if d <= a:
    forward = d
else:
    forward = d + (b*(d//a))

if d <= b:
    backward = d
else:
    backward = d + (a*(d//b))


print(forward + backward)
