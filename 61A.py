inLineOne = input()
inLineTwo = input()

i = 0

outLine = ""

while i < len(inLineOne):
    if inLineOne[i] == inLineTwo[i]:
        outLine = outLine + "0"
    elif inLineOne[i] != inLineTwo[i]:
        outLine = outLine + "1"

    i = i + 1

print(outLine)
