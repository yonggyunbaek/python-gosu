# https://softeer.ai/practice/6249

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dna = [ list(input().strip()) for _ in range(n)]

superDNA = [None for _ in range(2**n)]
superDNA[0] = ['.']*m

def merge(dna1,dna2):
    if dna1 == [] or dna2 == []:
        return []
    dna = []
    for i in range(m):
        if dna1[i] == '.':
            dna.append(dna2[i])
        elif dna2[i] == '.':
            dna.append(dna1[i])
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])
        else:
            return []
    return dna
        
def genSuperDNA(index):
    loc = 0
    tempIndex = index
    while tempIndex % 2 == 0:
        tempIndex = tempIndex//2
        loc += 1
    superDNA[index] = merge(dna[loc], superDNA[index-2**loc])

for i in range(1,2**n):
    genSuperDNA(i)

def genAnswer(index):
    if answer[index] < n+1:
        return answer[index]
    
    bit1 = []
    number1 = number2 = 0
    tempIndex = index
    for i in range(n):
        if tempIndex % 2 == 1:
            bit1.append(i)
            number2 += 2**i
        tempIndex = tempIndex//2

    digit = [0]*len(bit1)

    for i in range(1,2**(len(bit1)-1)):
        for j in range(len(bit1)):
            if digit[j] == 1:
                digit[j] = 0
                temp = 2**bit1[j]
                number1 -= temp
                number2 += temp
            else:
                digit[j] = 1
                temp = 2**bit1[j]
                number1 += temp
                number2 -= temp
                break
        temp = genAnswer(number1) + genAnswer(number2)

        if answer[index] > temp:
            answer[index] = temp
    return answer[index]

answer = [n+1]*(2**n)
answer[0] = 0

for i in range(1, 2**n):
    if superDNA[i] != []:
        answer[i] = 1
    else:
        genAnswer(i)
print(answer[2**n-1])