n = int(input())

s = input().lower()

if n < 26:
    print("NO")
    quit()

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpC = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 0

while i < len(s):
    ind = alp.index(s[i])
    alpC[ind] = alpC[ind] + 1

    i = i + 1

i = 0

while i < 26:
    if alpC[i] == 0:
        print('NO')
        quit()

    i = i + 1

print('YES')
