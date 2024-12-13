import sys
input = sys.stdin.readline

def strToSec(ms:str) -> int:
    m, s = map(int,ms.split(":"))
    return 60*m + s

def secToStr(sec:int) -> str:
    m = sec // 60
    s = sec % 60
    return str(m).zfill(2)+":"+str(s).zfill(2)

# 이기는 시간 집계
t1,t2=0,0
# 집계를 위한 임시값
tmp1,tmp2=0,0
# s가 양수면 1번이 이기는 상태, 음수면 2번이 이기는 상태, 0이면 비기는 상태
s=0

for i in range(int(input())):
    team, time = input().split()
    
    t = strToSec(time)
    if team=='1':
        if s == 0:
            s += 1
            tmp1 = t
        elif s != 0:
            s += 1
            if s == 0:
                t2 += t-tmp2
    else:
        if s==0:
            s-=1
            tmp2=t
        elif s!=0:
            s-=1
            if s==0:
                t1 += t-tmp1  

if s > 0:
    t1 += strToSec('48:00') - tmp1
elif s < 0:
    t2 += strToSec('48:00') - tmp2

print(str(secToStr(t1)))
print(str(secToStr(t2)))
