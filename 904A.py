import math

for _ in range(int(input())):
    lineIn = input().split()
    x = lineIn[0]
    k = int(lineIn[1])
    
    while True:
        summa = 0
        for i in x:
            summa = summa + int(i)
    
        if (summa % k == 0):
            print(x)
            break
        else:
            x = str(int(x) + 1)
        
