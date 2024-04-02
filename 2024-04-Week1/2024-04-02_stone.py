"""

"""

# 풀이 1 / brute force / 실패
import sys

N = int(sys.stdin.readline())
stone = list(map(int,sys.stdin.readline().split()))

if N == 1:
    print(1)

else:
    # 브루트 포스
    max_ans = 1
    for s in range(N):
        ans = 1

        max_s = stone[s]
        for n in range(s+1, N):
            if max_s < stone[n]:
                ans += 1
                max_s = stone[n]
        max_ans = max(max_ans, ans)
    print(max_ans)
    
#반례!!!!!!!!!!
"""
9
2 1 7 8 11 3 4 5 6
"""


# 풀이 2 / LIS

import sys

N = int(sys.stdin.readline())
stone = list(map(int,sys.stdin.readline().split()))

if N == 1:
    print(1)

else:
    dp = [1] * N 
    
    # LIS
    for i in range(N):
        for j in range(i):
            if stone[j] < stone[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
    
    
"""
LIS가 뭘까?
최장 증가 부분 수열(Longest Increasing Subsequence, LIS)

예제
수열: 10, 20, 10, 30, 20, 50

이 수열에서 최장 증가 부분 수열을 찾아봅시다.

우선, 각 위치에 대해 최장 증가 부분 수열의 길이를 저장할 배열 dp를 만듭니다. 초기값은 모두 1로 설정합니다. 왜냐하면, 수열의 각 숫자 자체가 길이가 1인 증가하는 부분 수열이기 때문입니다.

초기 dp 상태: [1, 1, 1, 1, 1, 1]

이제, 수열의 두 번째 숫자부터 시작하여, 각 숫자가 이전 숫자들과 어떻게 증가하는 부분 수열을 이루는지 확인합니다.

20은 10보다 크므로, 10 뒤에 20을 이어붙여 길이가 2인 증가하는 부분 수열을 만들 수 있습니다.
다음 10은 이전의 어떤 숫자보다도 크지 않으므로, 증가하는 부분 수열의 길이를 늘릴 수 없습니다.
30은 10과 20 뒤에 이어붙일 수 있으므로, 길이가 3인 증가하는 부분 수열을 만들 수 있습니다.
20은 이전의 10 뒤에 이어붙일 수 있지만, 최장 길이를 늘리지는 못합니다.
마지막으로, 50은 10, 20, 30 뒤에 이어붙여 길이가 4인 최장 증가하는 부분 수열을 만들 수 있습니다.
각 단계에서 dp 상태 업데이트: [1, 2, 1, 3, 2, 4]
"""