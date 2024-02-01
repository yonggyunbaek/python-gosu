"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# binary tree1
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

#binary2
class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(1, n)

def binarySearch(self, left: int, right: int) -> int:
    if left == right:
        return left

    mid = (left + right) // 2

    if isBadVersion(mid):
        return self.binarySearch(left, mid)
    else:
        return self.binarySearch(mid + 1, right)

# timeout
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         for i in range(1, n+1):
#             if isBadVersion(i) == True:
#                 return i
#                 break
#             else:
#                 continue


"""
이진탐색 구현 방법 2가지
left = 1
right = n
target = ~~~

#1. 반복분 사용
while left =< right:
    mid = (left + right) // 2

    if mid > target:
        right = mid - 1
    elif mid < target:
        left = mid + 1
    else: # mid == target
        return mid

#2. 재귀함수
def binarySearch(target, left, right):
    if left > right:
        return False

    mid = (left + right) // 2

    if mid == target:
        return mid
    elif mid < target:
        left = mid + 1
    elif mid > target:
        right = mid - 1
        
    return binary_search(target, left, right) # 줄어든 범위를 더 탐색

#함수 호출
binary_search(target, start, end)
"""