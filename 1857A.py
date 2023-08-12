t = int(input())
i = 0

while i < t:
    n = int(input())
    numbers = input().split()

    j = 0
    sum = 0

    while j < n:
        sum = sum + int(numbers[j])
        j = j + 1

    if sum % 2 != 0:
        print('NO')
    else:
        print('YES')

    i = i + 1
