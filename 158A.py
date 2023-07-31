lineOne = input()
n = int(lineOne.split()[0])
k = int(lineOne.split()[1])

lineTwo = input()
scores = lineTwo.split()

qualScore = int(scores[k - 1])

qualCount = 0
i = 0

while i < n:
    if (int(scores[i]) >= qualScore) and (int(scores[i]) > 0):
        qualCount = qualCount + 1

    i = i + 1

print(qualCount) 
