"""
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(left, right):
    ans = 0
    
    for i in range(left, right + 1):
        # print(i)
        nums = []
        for j in range(1, int(i**(1/2))+1):
            if i%j==0:
                nums.append(i)
                if j < i//j:
                    nums.append(i//j)
        if len(nums) % 2 == 0:
            ans += i
        else:
            ans -= i
        
    return ans