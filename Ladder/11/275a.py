r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))

ma = [r1, r2, r3]

out = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

for i in range(3):
    for j in range(3):

        if ma[i][j] % 2 == 1:
            
             
            out[i][j] ^= 1
            if i != 0: out[i - 1][j] ^= 1
            if i != 2: out[i + 1][j] ^= 1
            if j != 0: out[i][j - 1] ^= 1
            if j != 2: out[i][j + 1] ^= 1

for l in out:
    for x in l: print(x, end="")
    print()
