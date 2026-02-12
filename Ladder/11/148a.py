from math import gcd
from functools import reduce

def lcm(a, b): return (a * b) // gcd(a, b)
def lcm2(a): return reduce(lcm, a)

k = int(input())
l = int(input())
m = int(input())
n = int(input())

ts = [k, l, m, n]

d = int(input())

s = sum([(d // x) for x in ts])

for i in range(4):
    for j in range(i + 1, 4):
        s -= (d // lcm(ts[i], ts[j])) 


for i in range(4):
    for j in range(i + 1, 4):
        for k in range(j + 1, 4):
            s += (d // lcm2([ts[i], ts[j], ts[k]])) 

s -= (d // lcm2(ts))

print(s)
