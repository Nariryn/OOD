def power(index,inp):
    if index >= len(inp):
        return 0
    return power(2*index+1,inp) + inp[index] + power(2*index+2,inp)

k,cm = input("Enter Input : ").split("/")
k = [int(i) for i in k.split(" ")]
cm = cm.split(",")
print(power(0,k))
for i in cm:
    f,s = i.split(" ")
    f = int(f)
    s = int(s)
    if power(f,k) > power(s,k):
        print(f'{f}>{s}')
    elif power(f,k) == power(s,k):
        print(f'{f}={s}')
    else:
        print(f'{f}<{s}')