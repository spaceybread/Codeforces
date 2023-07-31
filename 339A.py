numbers = input().split('+')
numbers.sort()
 
i = 0
stringPrint = ''
 
while i < (len(numbers) - 1):
    stringPrint = stringPrint + numbers[i] + '+'
    i = i + 1
 
stringPrint = stringPrint + numbers[-1]
 
print(stringPrint)
