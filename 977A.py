inNum = input().split()

n = int(inNum[0])
iter = int(inNum[1])

i = 0

while i < iter:
    if n % 10 == 0:
        n = n/10
    else:
        n = n - 1
    i = i + 1

print(int(n)) 
