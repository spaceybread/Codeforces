inLine = (input())

out = False

if 'H' in str(inLine):
    out = True
if 'Q' in str(inLine):
    out = True
if '9' in str(inLine):
    out = True

if out == True:
    print('YES')
else:
    print('NO')
