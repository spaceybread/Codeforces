wordIn = input()
wordOut = input()

expectedWord = []
i = len(wordIn)

while i > 0:
    expectedWord.append(wordIn[i - 1])
    i = i - 1

expecWord = ''.join(expectedWord)

if expecWord in wordOut:
    print('YES')
else:
    print('NO')
