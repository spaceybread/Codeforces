import math
 
input = input()
inputList = input.split()
 
area = int(inputList[0]) * int(inputList[1])
 
domino = math.floor(area/2)
print(domino)
