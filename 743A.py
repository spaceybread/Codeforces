games = int(input())
wrIn = input()


i = 0
wr = []

while i < games:
    wr.append(wrIn[i])
    i = i + 1

anton = wr.count('A')
thresh = games/2

if anton == thresh:
    print('Friendship')
elif anton > thresh:
    print('Anton')
else:
    print('Danik')
