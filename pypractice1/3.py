print(' *** String count ***')
passage = input('Enter message : ')
upper = []
lower = []
count_upper = 0
count_lower = 0
for i in passage:
    if i.isupper() == True:
        count_upper += 1
        if i not in upper:
            upper.append(i)
    if i.islower() == True:
        count_lower += 1
        if i not in lower:
            lower.append(i)
print(f'No. of Upper case characters : {count_upper}')
print('Unique Upper case characters : ',end='')
upper.sort()
for j in upper:
    print(j,end='  ')
print('')
print(f'No. of Lower case Characters : {count_lower}')
print('Unique Lower case characters : ',end='')
lower.sort()
for k in lower:
    print(k,end='  ')