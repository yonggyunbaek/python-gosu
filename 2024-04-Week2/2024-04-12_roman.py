class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {'I': 1,
                 'IV': 4,
                 'V': 5,
                 'IX': 9,
                 'X': 10,
                 'XL': 40,
                 'L': 50,
                 'XC': 90,
                 'C': 100,
                 'CD': 400,
                 'D': 500,
                 'CM': 900,
                 'M': 1000}
        
        ans = []
       
        while num >= 1:
            if num >= 1000:
                ans.append('M')
                num -= 1000
            elif num >= 900:
                ans.append('CM')
                num -= 900
            elif num >= 500:
                ans.append('D')
                num -= 500
            elif num >= 400:
                ans.append('CD')
                num -= 400
            elif num >= 100:
                ans.append('C')
                num -= 100
            elif num >= 90:
                ans.append('XC')
                num -= 90
            elif num >= 50:
                ans.append('L')
                num -= 50
            elif num >= 40:
                ans.append('XL')
                num -= 40
            elif num >= 10:
                ans.append('X')
                num -= 10
            elif num >= 9:
                ans.append('IX')
                num -= 9
            elif num >= 5:
                ans.append('V')
                num -= 5
            elif num >= 4:
                ans.append('IV')
                num -= 4
            elif num >= 1:
                ans.append('I')
                num -= 1
        
        return ''.join(ans)