import math
 
input = input()
inputList = input.split()
k = int(inputList[0])
n = int(inputList[1])
w = int(inputList[2])
 
i = 1
total = 0
while i <= w:
    total = total + i * k
    i = i + 1
 
 
moneyReq = total - n
 
if moneyReq <= 0:
    print('0')
else:
    print(moneyReq)
