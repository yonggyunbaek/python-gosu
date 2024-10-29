# https://leetcode.com/problems/convert-date-to-binary/submissions/
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_list = map(int,date.split('-'))
        answer = []
        for d in date_list:
            answer.append(bin(d)[2:])

        return '-'.join(answer)
