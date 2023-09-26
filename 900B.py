def construct_array(n):
    if n < 3:
        return []

    a = [0] * (n + 1)
    a[1] = 2
    a[2] = 3
    a[3] = 6

    for i in range(4, n + 1):
        a[i] = i + 3

    return a[1:]

t = int(input())
for _ in range(t):
    n = int(input())
    result = construct_array(n)
    print(" ".join(map(str, result)))
