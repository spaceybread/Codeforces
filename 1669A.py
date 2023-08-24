n = int(input())
i = 0

while i < n:
    a = int(input())

    if a >= 1900:
        print("Division 1")
    elif a >= 1600:
        print("Division 2")
    elif a >= 1400:
        print("Division 3")
    else:
        print("Division 4")
    i = i + 1
