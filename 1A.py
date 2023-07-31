import math

input = input()
inputList = input.split()

inN = math.ceil(int(inputList[0])/int(inputList[2]))
inM = math.ceil(int(inputList[1])/int(inputList[2]))

tiles = inM * inN

print(tiles)
