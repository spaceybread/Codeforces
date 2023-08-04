import math
valsIn = input().split()

coord1 = [int(valsIn[0]), int(valsIn[1])]
coord2 = [int(valsIn[2]), int(valsIn[3])]
coord3 = []
coord4 = []
d = 0

if coord1[0] == coord2[0]:
    #adjacten points in x
    d = abs(coord1[1] - coord2[1])
    coord3 = [coord1[0] + d, coord1[1]]
    coord4 = [coord2[0] + d, coord2[1]]
    print("{} {} {} {}".format(coord3[0], coord3[1], coord4[0], coord4[1]))

elif coord1[1] == coord2[1]:
    #adjacten points in x
    d = abs(coord1[0] - coord2[0])
    coord3 = [coord1[0], coord1[1] + d]
    coord4 = [coord2[0], coord2[1] + d]
    print("{} {} {} {}".format(coord3[0], coord3[1], coord4[0], coord4[1]))

elif coord1[0] != coord2[0] and coord1[1] != coord2[1]:
    if abs(coord1[0] - coord2[0]) == abs(coord1[1] - coord2[1]):
        #opposite corners
        coord3 = [coord1[0], coord2[1]]
        coord4 = [coord2[0], coord1[1]]
        print("{} {} {} {}".format(coord3[0], coord3[1], coord4[0], coord4[1]))

    else:
        print(-1)
else:
    print(-1)
