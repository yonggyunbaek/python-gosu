"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans_list = []
        
        for i in range(1,n+1):
            tmp = ""
            if i % 3 == 0:
                tmp += "Fizz"
            if i % 5 == 0:
                tmp += "Buzz"
            
            if tmp != "":
                ans_list.append(tmp)
            else:
                ans_list.append(str(i))
        return ans_list