x,y = input("enter number : ").split(',')
x = int(x)
y = int(y)

def gcd(x,y):
    if y == 0:
        if x > 0:
            return x
        else:
            return x*-1
    else:
        return gcd(y,x%y)

print(gcd(x,y))