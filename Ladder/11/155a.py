n = int(input())
a = list(map(int, input().split()))

mi, ma = a[0], a[0]
c = 0

for i in range(1, n):
    v = a[i]

    if a[i] > ma: 
        ma = a[i]
        c += 1

    if a[i] < mi: 
        mi = a[i]
        c += 1

print(c)
