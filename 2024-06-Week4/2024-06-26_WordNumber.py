"""
Suppose that a string s consisting of both lower-case and upper-case letters are given. 
Write a function "solution" to return True when the number of 'p' and 'y' in s are the same, and return False otherwise. Note that when there is neither 'p' nor 'y', it should always return True. Also, when comparing the number of 'p' and 'y', lower-case and upper-case are not distinguished.

For example, if s is "pPoooyY", then return true. In the case of "Pyy", return false.

Constraints
Length of string s : natural number less than 50.
String s consists of letters only.
"""

def solution(s):
    
    lower_s = s.lower()
    ans = 0
    for l in lower_s:
        if l == "p":
            ans += 1
        if l == "y":
            ans -= 1
    
    if ans == 0:
        return True
    
    else:
        return False