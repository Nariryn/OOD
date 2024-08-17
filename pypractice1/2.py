print(' *** Divisible number ***')
x = input('Enter a positive number : ')
num = int(x)
result = []
if num <= 0:
    print(f'{num} is OUT of range !!!')
else:
    for i in range(1,num+1):
        if num%i == 0:
            result.append(i)
    print('Output ==>',end=' ')
    for j in result:
        print(j,end=' ')
    l = len(result)
    print('')
    print(f'Total ==> {l}')
