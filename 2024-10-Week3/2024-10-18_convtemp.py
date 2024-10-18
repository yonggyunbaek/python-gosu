# https://leetcode.com/problems/convert-the-temperature/submissions/


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        def kelvin(celsius):
            return celsius + 273.15
        def Fahrenheit(celsius):
            return celsius * 1.80 + 32.00
        
        
        answer = []
        
        answer.append(kelvin(celsius))
        answer.append(Fahrenheit(celsius))
        
        return answer
