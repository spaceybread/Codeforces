word = input()
letter = word[0].upper()

i = 1
newWord = letter

while i < len(word):
    newWord = newWord + word[i]
    i = i + 1

print(newWord)
