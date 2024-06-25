"""
철호는 수열을 가지고 놀기 좋아합니다. 
어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 
원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.

원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

# 시간초과
def solution(elements):
    n = len(elements)
    result = set()

    # 길이가 1부터 n까지의 연속 부분 수열 합 계산
    for length in range(1, n+1):
        for i in range(n):
            partial_sum = 0
            for j in range(i, i+length):
                partial_sum += elements[j % n]
            result.add(partial_sum)

    return len(result)


# 통과
def solution(elements):
    answer = set()
    n = len(elements)
    # 원형 수열 생성
    elements = elements * 2
    for i in range(n):
        for j in range(n):
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)


## 다른 풀이
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)