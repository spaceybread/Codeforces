lowerList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

s = input()
i = 0
lowerCount = 0
upperCount = 0

while i < len(s):
    if s[i] in lowerList:
        lowerCount = lowerCount + 1
    else:
        upperCount = upperCount + 1
    i = i + 1

if upperCount > lowerCount:
    print(s.upper())
else:
    print(s.lower())
