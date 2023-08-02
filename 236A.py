lowerList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

usrnm = input()

count = 0
i = 0

while i < len(lowerList):
    if lowerList[i] in usrnm:
        count = count + 1
    i = i + 1

if count % 2 == 1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')
