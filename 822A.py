import math

inner = input().split()
a = int(inner[0])
b = int(inner[1])

if a >= b:
    print(math.factorial(b))
else:
    print(math.factorial(a))
