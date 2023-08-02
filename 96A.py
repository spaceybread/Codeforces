teamStr = input()

i = 0
team = []
while i < len(teamStr):
    team.append(int(teamStr[i]))
    i = i + 1

baseIndex = 0

while baseIndex < len(team) - 1:
    iter = 0
    adjCount = 1

    baseVal = team[baseIndex]
    while (baseIndex + iter) < len(team) and adjCount > 0:
        if baseVal == team[baseIndex + iter]:
            adjCount = adjCount + 1
            if adjCount > 7:
                print('YES')
                exit()
        else:
            adjCount = 0

        iter = iter + 1

    baseIndex = baseIndex + 1

print('NO')
