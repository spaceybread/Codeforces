n = int(input())
inputWords = []

i = 0
while i < n:
    inputWords.append(input())
    i = i + 1

i = 0

while i < n:
    wordProc = inputWords[i]
    length = len(wordProc)
    if length > 10:
        alteredWord = "{}{}{}".format(wordProc[0], int(length-2), wordProc[-1])
        print(alteredWord)
    else:
        print(wordProc)
    i = i + 1
