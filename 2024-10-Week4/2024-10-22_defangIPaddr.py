# https://leetcode.com/problems/defanging-an-ip-address/submissions/
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = address.split(".")
        
        return '[.]'.join(ans)
