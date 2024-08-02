from math import gcd
def lcm(a,b):
    return (a * b) // gcd(a,b)

def solution(n, m):
    answer = []
    ans1 = gcd(n, m)
    ans2 = lcm(n, m)
    # print(ans1,ans2)
    answer.append(ans1)
    answer.append(ans2)
    return answer
