"""
https://softeer.ai/app/assessment/index.html?xid=123591&xsrfToken=z9cF8Zk58r6n5QzfzAIxj6GZbgjSMsr6&testType=practice
"""

# 풀이 1 / timeout
import sys
N = int(sys.stdin.readline())

ans = ''
for _ in range(N):
    # A, B = sys.stdin.readline().split()
    # A, B = A.upper(), B.upper()
    A, B = sys.stdin.readline().split()

    # O(N)이 됨.
    ans += B[A.index('X')]
    # ans += B[A.find('X')] 같다.
print(ans)            
# 5.093 초	200.00 MB



# 풀이 2 / 성공
import sys

N = int(sys.stdin.readline())
ans = []

for _ in range(N):
    A, B = sys.stdin.readline().strip().upper().split()  # 입력을 받자마자 대문자로 변환

    for i in range(len(A)):
        if A[i] == 'X':  # 대문자로 변환했으므로 'X'만 확인하면 됨
            ans.append(B[i])
            break

print(''.join(ans))  # 이미 모든 문자가 대문자이므로, 여기서 .upper() 호출은 필요 없음

# 0.332 초	84.00 MB


"""
왜 ans += '문자열'과 list.append('문자열') > ''.join(list)가 속도에서 큰 차이가 발생할까?

아주 기본적이고 중요한 조건. 
- 문자(String)은 불변(Immutable) 객체
- 배열(list)은 가변(mutable) 객체 이다.

즉, ans += '문자열' 코드가 loop에 의해 반복 수행이 되면, ans라는 변수에 문자열이 추가 될 때 마다 새로운 메모리에 적재하게 된다.
하지만, 배열에 요소를 저장하게 되면, 파이썬의 경우에 연속된 메모리 객체에 해당 값을 저장하는게 아니고, 그 요소(element)의 주소값을 저장하기 때문에 시간, 메모리 모두 적게 사용할 수 있다.
"""