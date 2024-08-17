def find_gcd(f,s):
    if s==0:
        if f > 0: 
            return f
        else:
            return f*-1
    else:
        return find_gcd(s,f%s)
first,second = input("Enter Input : ").split(" ")
Gcd = find_gcd(int(first),int(second))
if int(first) == 0 and int(second) == 0:
    print("Error! must be not all zero.")
elif int(first)>int(second):  
    print(f'The gcd of {first} and {second} is : {Gcd}')
else:
    print(f'The gcd of {second} and {first} is : {Gcd}')