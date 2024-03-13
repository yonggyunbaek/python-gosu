"""
문제

회사 식당에는 전설처럼 전해 내려오는 비밀 메뉴에 대한 소문이 있다. 소문의 내용은 대강 이러하다.
식권 자판기의 버튼을 특정 순서대로 누르고 결제를 하면, 평소와는 다른 색깔의 식권이 나온다.
이 식권을 배식대에 제출하면, 어떤 비밀 메뉴를 받을 수 있다는 것이다. 물론 이를 실제로 본 사람은 아무도 없어서, 어떤 메뉴가 나오는지는 커녕 눌러야 하는 버튼의 순서조차 알려져 있지 않다.

주방장인 당신은 이 소문의 실체를 알고 있다. 이는 분명한 사실이다!
정해진 버튼 조작법을 사용하면 비밀 메뉴의 식권을 얻을 수 있다. 그러나 얼마 전 식권 자판기가 고장으로 교체되면서, 새 자판기에서는 비밀 메뉴 조작법이 작동하지 않게 되었다.
당신은 프로그래밍 실력을 살려, 사용자의 버튼 조작 중 비밀 메뉴 조작법이 포함되어 있는지를 판단하는 회로를 추가하려 한다.

자판기에는 총 K개의 버튼이 있다. 각 버튼마다 1부터 K까지 번호가 붙어 있어서, 조작 과정은 1 이상 K 이하의 정수 여러 개로 나타낼 수 있다.
비밀 메뉴 조작법은 M개의 버튼 조작으로 이루어져 있으며, 이 순서대로 버튼을 누르면 반드시 비밀 메뉴 식권이 발매된다. 이때, 이 조작법 앞뒤로 다른 버튼 조작이 있어도 비밀 메뉴로 인정된다.
사용자가 누른 N개의 버튼 조작이 주어질 때, 사용자가 비밀 메뉴 식권을 받을 수 있는지를 확인하는 프로그램을 작성하여라.

제약조건
1 <= K <= 9
1 <= M <= 100
1 <= N <= 100

각 버튼의 번호는 1 이상 K 이하이다.
"""

import sys
"""
M: password length
N: input_pw length
K: button num
""" 
M, N, K = map(int,sys.stdin.readline().split())
password = list(map(int,sys.stdin.readline().split()))
input_pw = list(map(int,sys.stdin.readline().split()))
# print(K,M,N)
# print(password)
# print(input_pw)

ans = "normal"
for ip in range(N - M + 1):
    # print(input_pw[ip])
    if input_pw[ip:ip+M] == password:
        ans = "secret"
        break

print(ans)