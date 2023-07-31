import math
 
x = int(input())
 
if (x % 5 == 0):
    steps = int(x/5)
    print(steps)
else:
    steps = math.floor(x/5) + 1
    print(steps)
