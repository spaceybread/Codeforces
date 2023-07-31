n = int(input())
problems = []

i = 0
while i < n:
    problems.append(input())
    i = i + 1

solve = 0

i = 0
while i < n:
    parts = problems[i]
    partsList = parts.split()
    count = 0

    j = 0
    while j < 3:
        a = int(partsList[int(j)])
        if a == 1:
            count = count + 1
        j = j + 1

    if count > 1:
        solve = solve + 1
    i = i + 1
print(solve)
