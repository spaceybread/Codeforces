for _ in range(int(input())):
    s = input()
    print(s) if len(s) < 11 else print(s[0] + str(len(s) - 2) + s[-1])
