print ("*** Fun with Drawing ***")
num = int(input("Enter input : "))

print("."*(num-1) + "*" + "."*(2*(num)-3) + "*" + "."*(num-1))

for i in range(num-2, 0, -1):
    print("."*(i) + "*" + "+"*(2*(num-i-2)+1) + "*" + "."*(2*(i)-1) + "*" + "+"*(2*(num-i-2)+1) + "*" + "."*(i))

print("*" + "+"*(2*(num)-3) + "*" + "+"*(2*(num)-3) + "*")

for i in range(1, 2*num-2):
    print("."*(i) + "*" + "+"*(2*((2*num-3)-i)+1) + "*" + "."*(i))

print("."*(2*num-2) + "*" + "."*(2*num-2))