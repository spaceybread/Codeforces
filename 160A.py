def summer(array, index):
    a = 0
    b = 0

    j = 0

    while j < index:
        a = a + array[j]
        j = j + 1

    while j < len(array):
        b = b + array[j]
        j = j + 1


    if b > a:
        return True
    else:
        return False



n = int(input())

li = input().split()

i = 0

while i < n:
    li[i] = int(li[i])
    i = i + 1

li.sort()

i = n

while i > 0:
    i = i - 1
    if summer(li, i) == True:
        print(n - i)
        quit()
