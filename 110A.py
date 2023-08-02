def countCheck(lst):
    n = lst.count(4) + lst.count(7)
    if n == 4 or n == 7:
        print('YES')
        exit()
    else:
        print('NO')
        exit()

valueIn = input()

i = 0
value = []

while i < len(valueIn):
    value.append(int(valueIn[i]))
    i = i + 1

countCheck(value)

#made me realise that sometimes, the problem isn't the implementation but rather the possibility that I didn't understand the problem correctly
