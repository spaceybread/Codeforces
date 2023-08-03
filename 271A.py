def yearSplit(year):
     thou = int((year - year % 1000)/1000)
     a = year - thou*1000
     hund = int((a - a % 100)/100)
     a = year - thou*1000 - hund*100
     tens = int((a - a % 10)/10)
     ones = year - thou*1000 - hund*100 - tens*10

     return [thou, hund, tens, ones]


yearVal = int(input())

while True:
    yearVal = yearVal + 1
    numbs = yearSplit(yearVal)

    if numbs[0] != numbs[1] and numbs[0] != numbs[2] and numbs[0] != numbs[3] and numbs[1] != numbs[2] and numbs[1] != numbs[3] and numbs[2] != numbs[3]:
        print(yearVal)
        exit()
