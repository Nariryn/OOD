def binary_number(n, prefix = ''):
    if n == 0:
        print (prefix)
    else:
        binary_number(n-1, prefix + '0')
        binary_number(n-1, prefix + '1')

n = int(input("Enter Number : "))

if n < 0:
    print("Only Positive & Zero Number ! ! !")
elif n == 0:
    print("0")
else:
    binary_number(n)