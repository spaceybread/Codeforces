from math import sqrt

l = int(input())
numList = input().split()

i = 0

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    k = 3
    while k < int(sqrt(n))+1:
        if n % k == 0:
            return False
        k = k + 2

    return True


while i < l:
    number = int(numList[i])

    if number % 2 == 0 and number != 4:
            print('NO')
    else:
        sqrRt = sqrt(number)

        if sqrRt % 1 != 0 or sqrRt == 1:
            print('NO')
        else:
            if isPrime(sqrRt) == True:
                print('YES')
            else:
                print('NO')

    i = i + 1
