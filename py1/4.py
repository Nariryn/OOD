print('*** Fun with Drawing ***')
x = input('Enter input : ')
num = 2*int(x)-1
for i in range(num,0,-1):
    for j in range(num-i):
        if j%2 == 0 or j == 0:
            print('#',end='')
        else:
            print('.',end='')
    for j in range(1,i*2):
        if i%2 == 0 or i == 0:
            print(".",end='')
        else:
            print('#',end='')
    for j in range(num-i,0,-1):
        if j%2 == 0 or j == 0:
            print('.',end='')
        else:
            print('#',end='')
    print('')
for i in range(2,num+1):
    for j in range(num-i):
        if j%2 == 0 or j == 0:
            print('#',end='')
        else:
            print('.',end='')
    for j in range(1,2*i):
        if i%2 == 0 or i == 0:
            print(".",end='')
        else:
            print('#',end='')
    for j in range(num-i,0,-1):
        if j%2 == 0 or j == 0:
            print('.',end='')
        else:
            print('#',end='')
    print('')