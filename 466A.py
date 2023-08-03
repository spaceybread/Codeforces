import math

inner = input().split()
n = int(inner[0])
m = int(inner[1])
a = int(inner[2])
b = int(inner[3])

initial = math.floor(n/m)
if a*n > initial*b:
    nCost = (n%m)*a
    if nCost > b:
        print(initial*b + b)
    else:
        print(initial*b + nCost)
else:
    print(a*n)
