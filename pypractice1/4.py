print('*** String Rotation ***')
x,y =input('Enter 2 strings : ').split()

count = 1

finalx = x[len(x)-2:len(x)]+x[0:len(x)-2] 
finaly = y[3:len(y)]+y[0:3]
print(f'{count} {finalx} {finaly}')

while True:
    finalx = finalx[len(x)-2:len(x)]+finalx[0:len(x)-2] 
    finaly = finaly[3:len(y)]+finaly[0:3]
    count+=1
    if finalx == x and finaly == y:
        print(f'{count} {finalx} {finaly}')
        print(f'Total of  {count} rounds.')
        break
    if count<5:
        print(f'{count} {finalx} {finaly}')
    elif count == 5:
        print(f'{count} {finalx} {finaly}')
        print(' . . . . .')
    