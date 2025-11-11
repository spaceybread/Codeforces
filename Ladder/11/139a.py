n = int(input())
a = list(map(int, input().split()))

n = n % sum(a)

if n == 0: 
    for i in range(6, -1, -1):
        if a[i] != 0:
            print(i + 1)
            quit()


for i in range(len(a)):
    n -= a[i]

    if n <= 0: 
        print(i + 1)
        quit()

